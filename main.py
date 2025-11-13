import db
from bs4 import BeautifulSoup
import requests

codes = {
    # Dictionary containing the item name as the key and a tuple for screwfix and toolstation codes respectively
    0: {
        "name": "ptfe",
        "ts_code": 35444,
        "sf_code": 63859,
        "qty": 1,
        "pack_size": "10 rolls",
        "description": "plumber's tape",
    },
    1: {
        "name": "isolator_valve",
        "ts_code": 37336,
        "sf_code": 32802,
        "qty": 1,
        "pack_size": "10 valves",
        "description": "isolating valves",
    },
}


def get_item_prices(ts_code: int, sf_code: int) -> tuple:
    ts_price = get_ts_price(ts_code)
    sf_price = get_sf_price(sf_code)
    return (ts_price, sf_price)


def get_sf_price(code: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }
    url = f"https://www.screwfix.com/p/{code}"
    print(url)
    request = requests.get(url=url, headers=headers)
    if request.status_code == 200:
        data = request.text
        soup = BeautifulSoup(data, "html.parser")
        price_left = soup.find(class_="_U1S20")
        price_left_string = price_left.contents[0]
        price_right = soup.find(class_="xIIluZ")
        price_right_string = price_right.contents[2]
        price_string = f"{price_left_string}.{price_right_string}"
        price = int(float(price_string) * 100)
        return price
    else:
        print(f"Failed with status code {request.status_code}")
        return


def get_ts_price(code: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }
    url = f"https://www.toolstation.com/p{code}"
    print(url)
    request = requests.get(url=url, headers=headers)
    if request.status_code == 200:
        data = request.text
        soup = BeautifulSoup(data, "html.parser")
        toolstation_price_unparsed = soup.find("span", class_="md:text-size-9")
        toolstation_price = float(toolstation_price_unparsed.text.lstrip()[1:])
        return int(toolstation_price * 100)
    else:
        print(f"Failed with status code {request.status_code}")
        return


def main():
    # db.create_products_table()
    # for i in codes:
    #     db.insert_new_product(
    #         codes[i]["name"],
    #         codes[i]["ts_code"],
    #         codes[i]["sf_code"],
    #         codes[i]["qty"],
    #         codes[i]["pack_size"],
    #         codes[i]["description"],
    #     )

    all_products = db.get_all_products()
    for product in all_products:
        # 3 & 5 for prices
        print(product[2], product[4])
        scraped_prices = (get_item_prices(product[2], product[4]))
        


if __name__ == "__main__":
    main()

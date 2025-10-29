from bs4 import BeautifulSoup
import requests

codes = {
    # Dictionary containing the item name as the key and a tuple for screwfix and toolstation codes respectively
    "ptfe": ("63859", "35444")
}


def get_item_prices(sf_code, ts_code):
    sf_price = get_sf_price(sf_code)
    ts_price = get_ts_price(ts_code)
    return (sf_price, ts_price)


def get_sf_price(code):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }
    url = f"https://www.screwfix.com/p/{code}"
    request = requests.get(url=url, headers=headers)
    print(request.status_code)
    if request.status_code == 200:
        data = request.text
        soup = BeautifulSoup(data, "html.parser")
        price_left = soup.find(class_="_U1S20")
        price_left_string = price_left.contents[0]
        price_right = soup.find(class_="xIIluZ")
        price_right_string = price_right.contents[2]
        price_string = f"{price_left_string}.{price_right_string}"
        return price_string


def get_ts_price(code):
    pass


def main():
    sf_price = get_sf_price(codes["ptfe"][0])


if __name__ == "__main__":
    main()

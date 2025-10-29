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
    if request.status_code == 200:
        data = request.text
        soup = BeautifulSoup(data, "html.parser")
        price_left = soup.find(class_="_U1S20")
        price_left_string = price_left.contents[0]
        price_right = soup.find(class_="xIIluZ")
        price_right_string = price_right.contents[2]
        price_string = f"{price_left_string}.{price_right_string}"
        return price_string
    else:
        print(f"Failed with status code {request.status_code}")
        return


def get_ts_price(code):
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
        return toolstation_price
    else:
        print(f"Failed with status code {request.status_code}")
        return


def main():
    # sf_price = get_sf_price(codes["ptfe"][0])
    ts_price = get_ts_price(codes["ptfe"][1])


if __name__ == "__main__":
    main()

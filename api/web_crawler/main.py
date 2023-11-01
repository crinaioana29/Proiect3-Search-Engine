import requests
import pandas as pd
from bs4 import BeautifulSoup
from .request_model import RequestModel
from unidecode import unidecode

def web_scrapping(word):
    try:
        rq = RequestModel(path='resources/ConfigFile.properties', request_section='RequestSection')
        headers = {'User-Agent': rq.headers}
        page = requests.get(rq.hostname + word + rq.params, headers=headers)
        page.raise_for_status()  # Raise an exception if the request was not successful

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="list_cart_holder")

        listing_data = results.find_all('a', class_="main_items")
        df = scrape_data_to_dataframe(listing_data)

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return df

def scrape_data_to_dataframe(listing_data):
    data_list = []
    data = {}
    for l_a in listing_data:
        title = l_a.find("span", class_="title")
        price = l_a.find("span", class_="price shadow")
        if title is not None and price is not None:
            data = {"Title": unidecode(title.text.strip()),
                    "Price": unidecode(price.text[4:].strip())}

        data_list.append(data)
    return data_list
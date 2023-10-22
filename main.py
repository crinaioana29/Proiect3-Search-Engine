import requests
from bs4 import BeautifulSoup

URL = "https://lajumate.ro/cauta_casa_ordonare-dupa-data-descrescator.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

try:
    page = requests.get(URL, headers=headers)
    page.raise_for_status()  # Raise an exception if the request was not successful

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="list_cart_holder")

    listing_data = results.find_all('a', class_="main_items")

    for l_a in listing_data:
        title = l_a.find("span", class_="title")
        price = l_a.find("span", class_="price shadow")

        if title is not None and price is not None:
            print(title.text, price.text[4:])
        else:
            print("Incomplete data for a listing")
except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
except Exception as e:
    print(f"An error occurred: {e}")





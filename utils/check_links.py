import requests
from bs4 import BeautifulSoup
from sys import exit
from typing import List

BASE_URL = "https://nfdi4microbiota.github.io"
HOME_URL = f"{BASE_URL}/nfdi4microbiota-knowledge-base/"

# Go to base url
# get html
# get navbar
# get all links in navbar
# for each link
#     go to page
#     get all links
#     check if links return 200 or not
#     return list of links (and page) that do not return 200

def get_page_urls(url: str):
    response = requests.get(url)
    parsed_html = BeautifulSoup(response.text, 'html.parser')
    #print(parsed_html)
    page_urls = parsed_html(id = "sidebar-link")
    hrefs = [f'{BASE_URL}{url.get("href")}' for url in page_urls]
    return hrefs

def check_urls(hrefs: List[str]):
    for href in hrefs:
        print(href)
        response = requests.get(href)
        assert response
        exit(1)
    return None

def main():
    page_urls = get_page_urls(HOME_URL)
    broken_urls = check_urls(page_urls)

if __name__ == "__main__":
    main()
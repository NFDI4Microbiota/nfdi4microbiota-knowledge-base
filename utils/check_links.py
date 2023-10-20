import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from sys import exit
from typing import List

BASE_URL = "https://nfdi4microbiota.github.io"
HOME_URL = f"{BASE_URL}/"

def get_page_urls(url: str):
    response = requests.get(url)
    parsed_html = BeautifulSoup(response.text, 'html.parser')
    #print(parsed_html)
    page_urls = parsed_html(id = "sidebar-link")
    hrefs = [f'{BASE_URL}{url.get("href")}' for url in page_urls]
    return hrefs

def check_urls(page_urls: List[str]):
    page_to_broken_urls = {}
    for href in tqdm(page_urls):
        response = requests.get(href)
        assert response.status_code == 200, f"Got status code {response.status_code} from link: {href}"
        parsed_html = BeautifulSoup(response.text, 'html.parser')
        markdown_content = parsed_html.find('div', attrs={"id": "markdown-content"})
        anchors = markdown_content.findAll("a")
        urls = [anchor.get("href") for anchor in anchors]
        broken_urls = []
        print(f"Page url: {href}")
        for url in urls:
            try:
                r = requests.get(url)
                if r.status_code != 200:
                    print(f"Broken url: {url}")
                    print(f"Status Code: {r.status_code}")
                    broken_urls.append(url)
            except requests.exceptions.MissingSchema:
                # Ignore links to different sections of the same page
                if not url.startswith("#"):
                    print(f"Missing Schema url: {url}")
            except requests.exceptions.InvalidSchema:
                if not url.startswith("mailto:"):
                    print(f"Invalid schema url: {url}")
            except requests.exceptions.ConnectTimeout:
                print(f"Connection timeout: {url}")
            except requests.exceptions.SSLError:
                print(f"SSLerror: {url}")

        page_to_broken_urls[href] = broken_urls
    return page_to_broken_urls

def main():
    page_urls = get_page_urls(HOME_URL)
    broken_urls = check_urls(page_urls)
    print(broken_urls)

if __name__ == "__main__":
    main()

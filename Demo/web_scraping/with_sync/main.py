import aiohttp
import os
from bs4 import BeautifulSoup
import requests

def fetch_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Unable to fetch content from {url}. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def write_to_file(filename, content):
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # current_directory = "web_scraping/with_sync"
        directory = os.path.join(current_directory, "data")
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, filename)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def scrape_and_append(url, filename):
    content = fetch_content(url)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        prettified_content = soup.prettify()
        write_to_file(filename, prettified_content)
        print(f"Content from {url} has been added to {filename}")

def main():
    urls = [
        {
            "url": "https://hocpython.org/data/",
            "filename": "website_content_1.html"
        },
        {
            "url": "https://hhkungfu.site/",
            "filename": "website_content_2.html"
        }
    ]

    for url_info in urls:
        scrape_and_append(url_info["url"], url_info["filename"])

if __name__ == "__main__":
    main()

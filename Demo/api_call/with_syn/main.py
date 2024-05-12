import json
import os
import sys
import time
import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Unable to call API from URL: {url}\n")
            return None
    except requests.RequestException as e:
        print(f"Error connecting to {url}: {e}")
        return None

def save_data(url):
    data = fetch_data(url)
    if data:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(current_directory, "data")
        os.makedirs(directory, exist_ok=True)
        file_name = f"json_{url.split('/')[-1]}.json"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data from {url} has been saved to file '{file_name}'")
    else:
        print(f"Unable to fetch data from API: {url}")

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
    ]
    start = time.time()
    for url in urls:
        save_data(url)

    end = time.time()
    print(f"Total execution time: {end - start} seconds")

if __name__ == "__main__":
    main()

import requests
import time
def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Unable to call API from URL: {url}"
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")
        return None

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos"
    ]

    start = time.time()
    results = []
    for url in urls:
        result = fetch_data(url)
        results.append(result)

    print(results)
    end = time.time()
    print(f"Total execution time: {end - start} seconds")

if __name__ == "__main__":

    main()

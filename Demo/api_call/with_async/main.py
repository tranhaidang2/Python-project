import asyncio
import aiohttp
import json
import os
import sys
import time

async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Unable to call API from URL: {url}\n")
                return None
    except aiohttp.ClientConnectorError as e:
        print(f"Error connecting to {url}: {e}")
        return None

async def save_data(session, url):
    data = await fetch_data(session, url)
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

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
    ]
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [save_data(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end = time.time()
    print(f"Total execution time: {end - start} seconds")

if __name__ == "__main__":
    asyncio.run(main())

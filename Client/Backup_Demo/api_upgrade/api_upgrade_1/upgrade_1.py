import aiohttp
import asyncio
import time

async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return f"Unable to call API from URL: {url}\n"
    except aiohttp.ClientConnectorError as e:
        print(f"Error connecting to {url}: {e}")
        return None

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos"    
    ]

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    print(results)
    end = time.time()
    print()
    print(f"Total execution time: {end - start} seconds")
    
if __name__ == "__main__":
    asyncio.run(main())

# Code 404 : "https://example.com/invalidpage", "https://example.com/nonexistentpage"
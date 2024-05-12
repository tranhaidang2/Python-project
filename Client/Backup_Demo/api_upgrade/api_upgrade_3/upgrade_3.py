import aiohttp
import asyncio
import time

async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return f"Cannot call API for URL: {url}"
    except aiohttp.ClientConnectorError as e:
        print(f"Error connecting to {url}: {e}")
        return None

async def main():
    url = "https://jsonplaceholder.typicode.com/posts"

    start = time.time()
    async with aiohttp.ClientSession() as session:
        result = await fetch_data(session, url)

        if isinstance(result, list):
            for post in result:
                print("UserID:", post['userId'])
                print("Title: ", post['title'])
        else:
            print(result)

    end = time.time()
    print(f"Total execution time: {end - start} seconds")
    
if __name__ == "__main__":
    asyncio.run(main())

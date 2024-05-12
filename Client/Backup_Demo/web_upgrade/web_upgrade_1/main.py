import asyncio
import aiohttp
import os

async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def write_to_file(filename, content):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, filename)
    os.makedirs(current_directory, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

async def scrape_and_append(url, filename):
    content = await fetch_content(url)
    await write_to_file(filename, content)
    print(f"Content from {url} has been added to {filename}")

async def main():
    urls = [
                {
                    "url": "https://hocpython.org/data/",
                    "filename": "web_1.txt"
                },
                {
                    "url": "https://randomuser.me/",
                    "filename": "web_2.txt"
                }
            ]
    
    tasks = [scrape_and_append(url["url"], url["filename"]) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
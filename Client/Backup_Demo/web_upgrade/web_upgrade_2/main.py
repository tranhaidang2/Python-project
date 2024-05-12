import asyncio
import aiohttp
import os
from bs4 import BeautifulSoup

async def fetch_content(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching content from {url}: {e}")
        return None

async def write_to_file(filename, content):
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(current_directory, "data")
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, filename)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

async def scrape_and_append(session, url, filename):
    content = await fetch_content(session, url)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        prettified_content = soup.prettify()
        await write_to_file(filename, prettified_content)
        print(f"Content from {url} has been added to {filename}")

async def main():
    urls = []
    num_links = int(input("Enter the number of links: "))
    for i in range(num_links):
        url = input(f"Enter link {i+1}: ")
        filename = f"website_content_{i+1}.html"
        urls.append({"url": url, "filename": filename})

    async with aiohttp.ClientSession() as session:
        tasks = [scrape_and_append(session, url["url"], url["filename"]) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

    # https://hocpython.org/data/, https://hhkungfu.site/

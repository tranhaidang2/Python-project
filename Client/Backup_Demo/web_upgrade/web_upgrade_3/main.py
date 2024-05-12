import aiohttp
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://hocpython.org/data/"
    time_start = time.time()
    html = await fetch_data(url)
    
    # Use BeautifulSoup to parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the table and extract data
    table = soup.find('table')
    rows = table.find_all('tr')
    
    # Create a DataFrame from the data
    data = []
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    df = pd.DataFrame(data)
    
    # Save DataFrame to Excel file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    excel_file_path = os.path.join(current_directory, "data.xlsx")
    df.to_excel(excel_file_path, index=False, header=False)
    
    time_end = time.time()
    print(f"Total execution time: {time_end - time_start} seconds")

# Run the main function using asyncio
asyncio.run(main())

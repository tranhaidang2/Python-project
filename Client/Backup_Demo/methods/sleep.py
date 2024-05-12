
import asyncio

async def my_coroutine():
    print("Coroutine started")   
    await asyncio.sleep(2)  
    print("Coroutine finished")

async def main():
    await my_coroutine()

if __name__ == "__main__":
    asyncio.run(main())



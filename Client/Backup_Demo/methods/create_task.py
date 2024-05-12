
import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(2)
    print("Coroutine finished")

async def main():
    task = asyncio.create_task(my_coroutine())
    await task

if __name__ == "__main__":
    asyncio.run(main())

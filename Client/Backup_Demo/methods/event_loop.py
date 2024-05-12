import asyncio

async def my_coroutine():
    print("Coroutine started")   
    await asyncio.sleep(2)  
    print("Coroutine finished")

async def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print("Created Event Loop")

    await my_coroutine()

    loop.close()
    print("Closed Event Loop")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio

async def task_1():
    try:
        print("Task 1 started")
        await asyncio.sleep(2)
        print("Task 1 finished")
    except asyncio.CancelledError:
        print("Task 1 cancelled")

async def task_2():
    try:
        print("Task 2 started")
        await asyncio.sleep(4)
        print("Task 2 finished")
    except asyncio.CancelledError:
        print("Task 2 cancelled")

async def main():
    task1 = asyncio.create_task(task_1())
    shield = asyncio.shield(task1)
    task2 = asyncio.create_task(task_2())
    shield.cancel()
    task2.cancel()

if __name__ == "__name__":
    asyncio.run(main())

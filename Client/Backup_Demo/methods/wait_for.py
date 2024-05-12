
import asyncio

async def task_1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def run_task(task, timeout):
    try:
        await asyncio.wait_for(task(), timeout=timeout)
    except asyncio.TimeoutError:
        print(f"Timeout occurred in {task}")

async def main():
    await run_task(task_1, 3)
    await run_task(task_2, 3)

if __name__ == "__name__":
    asyncio.run(main())


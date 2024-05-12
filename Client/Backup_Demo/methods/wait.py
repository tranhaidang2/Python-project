
import asyncio

async def task_1():
    print("Task_1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")
    print("-------------")

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")
    print("-------------")

async def main():
    coroutines = [task_1(), task_2()]
    tasks = []
    for coro in coroutines:
        task = asyncio.create_task(coro)
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())





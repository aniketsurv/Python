import asyncio

async def fun1():
    print("fun1 start")
    task = asyncio.create_task(fun2())
    print("First")
    print("Second")
    await asyncio.sleep(2)
    print("Third")


async def fun2():
    print("Fun2 start")
    print("Four")
    print("Five")

asyncio.run(fun1())
import asyncio

async def fun1():
    print("fun1 start")
    await asyncio.sleep(15)
    print("one")

async def fun2():
    print("fun2 start")
    await asyncio.sleep(14)
    print("two")

async def fun3():
    print("fun3 start")
    await asyncio.sleep(1)
    print("three")

async def main():
    L = await asyncio.gather(
        fun1(),
        fun2(),
        fun3(),
    )
    print("Main End")

asyncio.run(main())
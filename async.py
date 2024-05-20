import time
async def any_func():
    async for i in range(100):
        await print(i)

start = time.time()
any_func()
end = time.time()
result = end - start
print('time: ' + str(result))
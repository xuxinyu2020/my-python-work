import asyncio

# 把generator标记为coroutine类型
import threading


@asyncio.coroutine
def hello():
    print('Hello Wolrd!(%s)' % threading.currentThread())
    r = yield from asyncio.sleep(1)
    # yield from后面必须跟生成器，而所以用asyncio.sleep(1)替代原来的time.sleep(1)
    print("Hello again!(%s)" % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

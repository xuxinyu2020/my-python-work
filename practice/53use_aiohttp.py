import asyncio

from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body='<h1>Index</h1>'.encode('utf-8'), content_type='text/html')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello,%s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


async def init():
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_get('/hello/{name}', hello)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)
    await site.start()
    print('Server started at http://127.0.0.1:8000...')
    return site


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()

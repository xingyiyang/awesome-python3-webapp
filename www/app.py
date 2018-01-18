#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
async web application.
'''
# 设置调试级别level,此处为logging.INFO,不设置logging.info()没有任何作用等同于pass
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

# @asyncio.coroutine把一个generator标记为coroutine类型，
# 然后，就把这个coroutine扔到eventloop中去执行
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    # yield from可以让我们方便的调用另一个generator
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(init(loop))
loop.run_forever()

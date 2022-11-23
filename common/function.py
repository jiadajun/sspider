#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
qcc 请求头生成
"""

import aiohttp
import asyncio
import random
import redis
from common.settings import RedisConfigure1

redis_client = redis.Redis(host=RedisConfigure1.HOST, port=RedisConfigure1.PORT, password=RedisConfigure1.PASSWORD)

class AsyncioFunc(object):
    async def post(session, url, headers=None, task=None, data=None, proxy=None):
        async with session.post(url, headers=headers, json=data, proxy=proxy) as response:
            return {
                "content": await response.json(),
                'task': task
            }

    async def get(session, url, headers=None, task=None, proxy=None):
        async with session.get(url, headers=headers, proxy=proxy) as response:
            return {
                "content": await response.text(),
                'task': task
            }


class IP():
    # 代理设置
    def get_ip_pool(self):
        ip_all = [item.decode() for item in redis_client.smembers('ip_list')]
        return ip_all




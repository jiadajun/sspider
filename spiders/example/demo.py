# coding:utf-8
import aiohttp
import asyncio
import logging
from common.function import AsyncioFunc
from common.spider_settings import Example
from common.function import IP

import random

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


async def main():
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
        # 获取任务
        tasks = Example.get_task(session)
        print(tasks)
        # 获取代理池
        get_ip_pool = IP.get_ip_pool(session)
        print(get_ip_pool)
        if tasks:
            aio_tasks = []
            for task in tasks:
                # 获取IP
                get_redis_IP = random.choice(get_ip_pool)
                proxy = f'http://{get_redis_IP}'
                # 获取请求方式 并填充请求信息
                request_type = AsyncioFunc.get(session, Example.url, Example.headers, task, proxy=proxy)
                aio_tasks.append(asyncio.ensure_future(request_type))
            if aio_tasks:
                tiktok_results = await asyncio.gather(*aio_tasks, return_exceptions=True)
            for index, item in enumerate(tiktok_results):
                try:
                    print(index, item)
                except Exception as e:
                    logging.exception(e)
                    continue

            await asyncio.sleep(2)
        else:
            print('暂无任务')
            await asyncio.sleep(60)
        return


while True:
    try:
        monitor_log_task = {}
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        logging.exception(e)

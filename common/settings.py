# -*- coding: utf-8 -*-

"""
CREATE YOUR DEFAULT_CONFIG !

Some configuration:
        CONCURRENT_REQUESTS     线程数量
        RETRIES                 重试次数
        DOWNLOAD_DELAY          下载延时
        RETRY_DELAY             重试延时
        DOWNLOAD_TIMEOUT        超时限制
"""

CONCURRENT_REQUESTS = 20


# 设置 redis 配置信息 多个库 就自由扩展

class RedisConfigure1():
    HOST = "127.0.0.1"
    PORT = 6379
    PASSWORD = "123456"
    DB = 0
    DECODE_RESPONSES = True


# mysql 配置信息

class MysqlConfigure1(object):
    HOST = "127.0.0.1"
    PORT = ""
    USERR = ""
    PASSWD = ""
    DB = ""

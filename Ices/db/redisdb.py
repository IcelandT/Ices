# -*- coding: utf-8 -*-
"""
@summary: 操作redis数据库
"""
import time
from typing import Union

import redis
from redis.connection import ConnectionError
from redis import Redis

import Ices.setting as settings
from Ices.utils.log import log


class RedisDB(object):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        db: int = 0
    ) -> None:
        """
        操作redis数据库

        Args:
            host (str): host
            port (int): port
            db (int): db

        Returns:
            None

        """
        if host is None:
            host = settings.REDIS_HOST
        if port is None:
            port = settings.REDIS_PORT
        if settings.REDIS_DB != 0:
            db = settings.REDIS_DB

        self.host = host
        self.port = port
        self.db = db

        # 获取redis连接
        self.redis_connect_pool = self.get_redis_connect_pool()

    def get_redis_connect_pool(self) -> Redis:
        """
        获取redis连接

        """
        if not self.host and self.port:
            raise ConnectionError("未设置redis连接信息")

        pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            db=self.db,
            max_connections=10
        )
        redis_connect = redis.Redis(connection_pool=pool, socket_connect_timeout=10)
        if redis_connect.ping():
            log.success("redis connect ✓")
            return redis_connect
        else:
            raise "redis连接失败"

    def z_add(self, name: Union[str, bytes], value: Union[str, bytes, memoryview, int, str]) -> None:
        """
        Zset, 使用有序集合存储数据, 会自动去重

        Args:
             name (Union[str, bytes]): 键名
             value (Union[str, bytes]): 值
        Returns:
            None

        """
        self.redis_connect_pool.zadd(name, {value: int(time.time() * 1000)})

    def z_range(self, name: Union[str, bytes], start: int, end: int, withscores: bool) -> str:
        """
        Zrange, 返回有序集合中分数最低的值

        Args:
            name (Union[str, bytes]): 键名
            start (int): 开始
            end (int): 结束
            withscores (bool): 为True时返回[值, 分数]列表, 为False时只返回值

        Returns:
            str

        """
        return self.redis_connect_pool.zrange(
            name=name,
            start=start,
            end=end,
            withscores=withscores
        )
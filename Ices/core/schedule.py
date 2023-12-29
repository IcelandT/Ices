# -*- coding: utf-8 -*-
"""
@summary: 爬虫请求调度器
"""
import json

from Ices.db.redisdb import RedisDB
from Ices.core.request import Request
from Ices.core.response import Response


class Schedule(object):
    def __init__(
        self,
        redis_key: str,
        concurrent_count: int,
    ):
        self.redis_key = redis_key
        self.concurrent_count = concurrent_count

        # 连接redis
        self.redis_db = RedisDB()

    def task_push_to_redis(self, request: Request) -> None:
        """
        将任务推送至redis中

        """
        request_dict = request.requests_dict
        self.redis_db.z_add(self.redis_key, json.dumps(request_dict))

    def process_request(self) -> None:
        """
        处理request, 从redis中拉取request任务 -> 去重 -> 请求 -> 判断返回是新的request还是item -> 将新的request入库

        """
        while self.redis_db.redis_connect_pool.exists(self.redis_key):
            # 从redis中拉取request任务
            request_tasks = self.redis_db.z_range(
                name=self.redis_key,
                start=0,
                end=self.concurrent_count - 1,
                withscores=False
            )
            request_tasks = [
                json.loads(request_task.decode("utf-8"))
                for request_task in request_tasks
            ]
            print(request_tasks)
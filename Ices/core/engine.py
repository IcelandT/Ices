# -*- coding: utf-8 -*-
"""
@summary: 爬虫引擎
"""
import time

from typing import Callable, Iterable

import Ices.setting as settings
from Ices.error.base_error import EmptyError
from Ices.utils.log import log
from Ices.core.schedule import Schedule


class Engine(object):
    def __init__(
        self,
        redis_key: str = None,
        concurrent_count: int = None,
        start_callback: Callable = None,
        end_callback: Callable = None
    ) -> None:
        """
        引擎初始化

        Args:
             redis_key (str): 爬虫任务数据存放在redis中的前缀
             concurrent_count (int): 爬虫并发数量
             start_callback (Callable): 爬虫开始时的回调
             end_callback (Callable): 爬虫结束时的回调

        Returns:
            None

        """
        self.redis_key = redis_key or settings.REDIS_KEY
        if not self.redis_key:
            raise EmptyError(
                """
                redis_key不能为空, 可在setting中添加配置, REDIS_KEY = "demo_spider"
                或在spider初始化时传承, XXXSpider(redis_key="demo_spider")
                """
            )

        self._start_request = None
        self.start_callback = start_callback
        self.end_callback = end_callback

        # 设置爬虫并发数量
        if concurrent_count:
            setattr(settings, "SPIDER_CONCURRENCY_COUNT", concurrent_count)
        self.concurrency_count = settings.SPIDER_CONCURRENCY_COUNT

        # 调度器实例化
        self.schedule = Schedule(
            redis_key=self.redis_key,
            concurrent_count=self.concurrency_count
        )

    def spider_begin(self) -> None:
        """
        爬虫启动时

        """
        if self.start_callback() is None:
            log.info("-------- spider project start --------")
            time.sleep(0.01)
        else:
            self.start_callback()

    def spider_end(self) -> None:
        """
        爬虫结束时

        """
        pass

    def start_task(self) -> None:
        """
        启动爬虫处理任务

        """
        self.spider_begin()
        # 判断start_request函数是否可迭代
        if not isinstance(self._start_request, Iterable):
            raise TypeError(
                """
                start_request必须为可迭代对象
                def start_request(self, request):
                    yield Ices.Request(url="www.baidu.com")
                """
            )

        for request_task in self._start_request:
            self.schedule.task_push_to_redis(request_task)

        self.schedule.process_request()
        self.spider_end()


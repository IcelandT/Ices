# -*- coding: utf-8 -*-
"""
@summary: spider 爬虫
"""
from typing import Iterable

from Ices.core.engine import Engine
from Ices.core.base_parser import BaseParser


class Spider(BaseParser, Engine):
    def __init__(
        self,
        redis_key: str = None,
        concurrent_count: int = None
    ) -> None:
        """
        爬虫初始化

        """
        super(Spider, self).__init__(
            redis_key=redis_key,
            concurrent_count=concurrent_count,
            start_callback=self.start_callback,
            end_callback=self.end_callback
        )

        self._start_request = self.start_request()

    def start(self) -> None:
        """
        对外暴露start方法

        """
        self.start_task()

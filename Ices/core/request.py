# -*- coding: utf-8 -*-
"""
@summary: 请求结构体
"""
from typing import List, Callable

from Ices.core.response import Response


class Request(object):
    _REQUEST_ATTRS_ = {
        "params",
        "data",
        "headers",
        "json",
        "proxies"
    }

    def __init__(
        self,
        url: str = "",
        method: str = "GET",
        retry_count: int = None,
        deduplication: bool = True,
        callback: Callable = None,
        **kwargs
    ) -> None:
        """
        构建Request请求体, engine将其传入schedule进行处理

        Args:
             ---
             url (str): url
             retry_count (int): 重试次数
             deduplication (bool): 是否去重(True/False)
             callback (Callable): 回调函数 (函数名称)
             ---
             以下参数与requests使用方式一致
             method (str): 请求方式 ("GET" / "POST"), 默认为"GET"
             params (dict): Query Parameters 查询字符串参数
             data (dict): Form Data 请求体
             headers (dict): 请求头
             json (dict): JSON类型请求体
             proxies (dict): 代理
             ---
             其他值, 用于传递其他参数
             **kwargs:

        Returns:

        """
        self.url = url
        self.method = method
        self.retry_count = retry_count
        self.deduplication = deduplication
        self.callback = callback

        # 处理传递的其他参数
        self.requests_kwargs = {}
        for requests_name, requests_value in kwargs.items():
            if requests_name in self._REQUEST_ATTRS_:
                self.requests_kwargs[requests_name] = requests_value

            self.__dict__[requests_name] = requests_value

    @property
    def requests_dict(self) -> dict:
        """
        将requests请求参数转成字典类型

        """
        requests_dict = {}

        callback_name = getattr(self.callback, "__name__")
        for requests_name, requests_value in self.__dict__.items():
            requests_dict[requests_name] = requests_value

        requests_dict["callback"] = callback_name
        return requests_dict

    def get_response(self) -> Response:
        """
        获取response

        """
        pass

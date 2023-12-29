# -*- coding: utf-8 -*-
"""
@summary: spider基类
"""


class BaseParser(object):
    def start_request(self):
        """
        添加初始请求的url

        Returns:
            Request: ices.Request(xxx)
        """
        pass

    def download_middleware(self, request):
        """
        下载中间件, 用于对请求做处理, 如添加cookie, headers等

        Args:
            request (): ices.Request(xxx)序列化后的request dict

        Returns:
            Request: request
        """
        pass

    def parse(self, request, response):
        """
        默认的解析函数

        """
        pass

    def start_callback(self):
        """
        框架开始的回调

        """
        pass

    def end_callback(self):
        """
        框架结束的回调

        """
        pass

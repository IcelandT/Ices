# -*- coding: utf-8 -*-
"""
@summary: 爬虫下载器, 将获取到的Response返回给引擎
"""

import asyncio
import aiohttp
from aiohttp import ClientResponse

from Ices.core.response import Response
from Ices.core.request import Request


class RequestsDownloader(object):
    async def download(self, request: Request) -> Response:
        response = aiohttp.request(
            request.method, request.url, **request.requests_kwargs
        )
        return Response(response)
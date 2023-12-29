# -*- coding: utf-8 -*-
"""
@summary: 日志
"""
from loguru import logger


class Log:
    @property
    def debug(self) -> logger:
        return logger.debug

    @property
    def success(self) -> logger:
        return logger.success

    @property
    def info(self) -> logger:
        return logger.info

log = Log()

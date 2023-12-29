# REDIS CONNECT CONFIG
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_USER_PASSWORD = ""
REDIS_DB = 0

# REDIS KEY NAME
REDIS_KEY = ""

# 爬虫相关
SPIDER_CONCURRENCY_COUNT = 5    # 爬虫并发数

# 导入用户 setting 文件
try:
    from setting import *
except:
    pass
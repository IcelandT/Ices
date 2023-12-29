import Ices
from Ices.utils.log import log


class TestSpider(Ices.Spider):
    def start_request(self):
        start_url = 'https://www.qidian.com/xuanhuan/'
        yield Ices.Request(
            url=start_url,
            deduplication=True,
            callback=self.parse
        )

    def parse(self, request, response):
        print(request)


if __name__ == '__main__':
    TestSpider(redis_key='xxx').start()

import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["reed.co.uk"]
    start_urls = ["https://reed.co.uk"]

    def parse(self, response):
        pass

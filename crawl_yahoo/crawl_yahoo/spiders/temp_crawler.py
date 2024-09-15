from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TempSpider(CrawlSpider):
    name = 'tmp_crawler'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://books.toscrape.com/']
    
    # PROXY_SERVER = "116.197.132.59"

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue/", deny="category"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "content": response.css(".price_color::text").get(),
        }


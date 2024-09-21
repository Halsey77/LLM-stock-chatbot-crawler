from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

def parse_time_element():
    return None

class CrawlingSpider(CrawlSpider):
    name = "my_crawler"
    allowed_domains = ["yahoo.com"]
    start_urls = ["https://finance.yahoo.com/"]
    download_timeout = 360

    # PROXY_SERVER = "116.197.132.59"

    rules = (Rule(LinkExtractor(allow="news"), callback="parse_item"),)

    def parse_item(self, response):
        date, time = response.css("time::attr(datetime)").get().split("T")
        time = time[:-1]
        
        yield {
            "title": response.css("#caas-lead-header-undefined::text").get(),
            "content": response.css("div.caas-body p::text").getall(),
            "date": date,
            "time": time,
            "link": response.url,
        }

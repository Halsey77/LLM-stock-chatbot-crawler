import scrapy

class YahooFinanceSpider(scrapy.Spider):
    name = 'yahoo_finance'
    start_urls = [
        'https://finance.yahoo.com/news/australian-boomers-retiring-less-half-230000729.html'
    ]

    def parse(self, response):
        # Get the full response body
        body = response.body
        
        # Save the response body to a file
        with open('response_body.html', 'wb') as f:
            f.write(body)
        
        # Optionally, print or return the body
        print(body)

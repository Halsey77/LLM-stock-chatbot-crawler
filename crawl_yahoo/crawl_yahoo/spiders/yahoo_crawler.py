from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

def parse_time_element():
    return None

class CrawlingSpider(CrawlSpider):
    name = "my_crawler"
    allowed_domains = ["yahoo.com"]
    start_urls = ["https://finance.yahoo.com/news/"]

    # PROXY_SERVER = "116.197.132.59"

    rules = (Rule(LinkExtractor(allow="news"), callback="parse_item"),)

    temp_body = [
        "(Bloomberg) -- About two thirds of Australian baby boomers leaving the workforce don’t have enough pension savings to retire comfortably, according to research from the industry’s peak body.",
        "Most Read from Bloomberg",
        "Slightly more than 30% of Australians are able to afford a comfortable lifestyle in retirement, the Association of Superannuation Funds of Australia said. The median pension account balance for men aged 60-64 sat at A$205,385 ($137,690) as of June 2022 and A$153,685 for women the same age, a ways off the industry’s accepted comfortable retirement standard of A$690,000 for couples and A$595,000 for singles.",
        "As the nation’s pension pool nears A$4 trillion, an estimated 2.5 million Australians are expected to retire in the next decade. The pension industry — known locally as superannuation — was made compulsory for all workers in 1992, with contributions equal to 3% of wages. The amount employers contribute has grown to 11.5% and will rise to 12% next year.",
        "Still, as the pension system matures and balances increase, the portion of people retiring with enough money to fund a comfortable lifestyle will rise to 50% or more by 2050, ASFA Chief Executive Officer Mary Delahunty said in an interview.",
        "“The people retiring now have not had a full benefit for their working life,” Delahunty said. “So they will still require a good level of government help, or help from the rest of us, to be able to retire with dignity.”",
        "Anxiety around retirement savings persists even as Australia regularly ranks among the world’s top pension systems. Some 40% of Australians say they’ll never have enough money to retire despite the country boasting one of the world’s most envied pensions systems, according to a Natixis Investment Managers survey released last week.",
        "“Lots of people are concerned about the comfort and ability of retirees at the moment because of the cost of living rises,” Delahunty said.",
        "Balances were down slightly in the 12 months to June 2022 compared to the previous year due to poor investment returns, but have since averaged an annual return of more than 9%, Delahunty said.",
        "Australia’s pension system is doing its part to relieve stress on the public purse. A 2023 government report found that despite the aging population, spending on pensions is projected to fall from 2.3% to 2% of gross domestic product within 40 years, as superannuation increasingly funds retirements.",
        "Still, a gender pay gap has fueled disparity in every age cohort’s pension pot, Delahunty said. The average balance for men is A$182,667, compared to A$146,146 for women, according to ASFA.",
        "A shortage of financial advisers also presents a challenge. The government has announced a range of proposed reforms for the sector.",
        "Most Read from Bloomberg Businessweek",
        "©2024 Bloomberg L.P.",
    ]

    def parse_item(self, response):
        date, time = response.css("time::attr(datetime)").get().split("T")
        time = time[:-1]
        
        yield {
            "title": response.css("#caas-lead-header-undefined::text").get(),
            "content": response.css("div.caas-body p::text").getall(),
            "date": date,
            "time": time,
        }

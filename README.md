# Scrapy spiders for crawling/scraping yahoo!finance

## Libraries used:
```
pip install scrapy proxyscrape scrapy-rotating-proxies
```

**Notes:** Follow this [issue](https://github.com/JaredLGillespie/proxyscrape/issues/34) to fix proxyscrape returning `none`.

## How to run:
"crawl_yahoo" is the main scrapy project with a yahoo spider `my_crawler`. Change `out.json` to the output file that you want.
```
cd crawl_yahoo
scrapy crawl my_crawler -o out.json
```
**Notes:** Using free proxies provided by proxyscrape is not reliable. Thus, the results might be different. The proxies are written in `proxies.txt` file, each has "ip:port" format.

# Scrapy spiders for crawling/scraping yahoo!finance

## Libraries used:
```
pip install scrapy proxyscrape scrapy-rotating-proxies
```

To use bertscore, install these libraries:
```
pip install bert-score sentencepiece
```

**Notes:** Follow this [issue](https://github.com/JaredLGillespie/proxyscrape/issues/34) to fix proxyscrape returning `none`.

## How to run:
"crawl_yahoo" is the main scrapy project with a yahoo spider `my_crawler`.
```
python run_crawler.py
```
The results are stored in an output json file named `output_{date}_{time}.json` inside `crawl_yahoo` folder.

**Notes:** Using free proxies provided by proxyscrape is not reliable. Thus, the results might be different. The proxies are written in `proxies.txt` file, each has "ip:port" format.

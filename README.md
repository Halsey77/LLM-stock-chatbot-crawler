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

### Running scraping process:
"crawl_yahoo" is the main scrapy project with a yahoo spider `my_crawler`.
```
python run_crawler.py
```
The results are stored in an output json file named `output_{date}_{time}.json` inside `crawl_yahoo/outputs` folder. There is also a log file for scrapy in `crawl_yahoo/logs` folder.

When scraping yahoo news, each sucessful scrape with return a json object:
```
{
    "title": "The title of the news",
    "content: "The content of the page",
    "date": "Date of upload in UTC+0",
    "time": "Time of upload in UTC+0",
    "link": "Link to the page"
}
```

**Notes:** Using free proxies provided by proxyscrape is not reliable. Thus, the results might be different. The proxies are written in `proxies.txt` file, each has "ip:port" format.

### Running Bertscore evaluation:
See more in `get_bert_score.py` file for implementation and basic uses.

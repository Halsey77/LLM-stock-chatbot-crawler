# Question-answer pair generation process

Below is an example how to generate question-answer based on the scraped news articles on Yahoo Finance.
Questions and answers were generated using **ChatGPT-4o**.

## 1. Prompt
Here is the prompt used:

> You are given an array of news in json format described as below:
> ```
> [
> 	{
> 		"title": "The title of the news",
> 		"content: "The content of the page",
> 		"date": "Date of upload in UTC+0",
> 		"time": "Time of upload in UTC+0",
> 		"link": "Link to the page"
> 	},
> 	{
> 		"title": "The title of the news",
> 		"content: "The content of the page",
> 		"date": "Date of upload in UTC+0",
> 		"time": "Time of upload in UTC+0",
> 		"link": "Link to the page"
> 	},...
> ]
> ```
> 
> Here is the array in json:
> ```
> [
>   {
>     "title": "Samsung Electronics estimates a 274% jump in Q3 operating profit",
>     "content": "SEOUL (Reuters) - Samsung Electronics estimated on Tuesday a 274% jump in third-quarter operating profit but > missed analyst estimates, as it struggled to capitalise on strong demand for chips used in artificial intelligence servers. > The world's largest memory chip, smartphone and TV maker estimated an operating profit of 9.1 trillion won ($6.78 billion) > for the three months ended Sept. 30, versus a 10.3 trillion won LSEG SmartEstimate. ($1 = 1,342.3700 won) (Reporting by > Hyunjoo Jin, Joyce Lee and Heekyong Yang; Editing by Christopher Cushing)",
>     "date": "2024-10-07",
>     "time": "23:56:15.000",
>     "link": "https://finance.yahoo.com/news/samsung-electronics-estimates-274-jump-235615435.html"
>   },
>   {
>     "title": "Oil prices extend gains as markets wait for Israel's retaliation against Iran",
>     "content": "Oil extended its gains on Monday following its biggest weekly gain in more than a year in anticipation of an > Israeli retaliation against Iran  . Separately, Hurricane Milton headed towards Florida off the gulf of Mexico strengthened > to Category 5, also helping fuel higher crude prices. West Texas Intermediate ( ) advanced more than 3% to close at $77.14 > per barrel after gaining more than 9% last week. Brent ( ), the international benchmark price, also advanced more than 3.5% > to settle at $80.93. Tel Aviv has vowed to strike back after Iran launched some 200 ballistic missiles toward Israel last > Tuesday. Oil futures have been moving on speculation of whether that retaliation will include targeting Iran's oil > infrastructure. \"The Iranian military has responded by saying any attack from Israel would trigger yet a stronger response > from Iran, so the geopolitical stages effect on crude continues to grow,\" Dennis Kissler, BOK Financial's senior vice > president of trading, wrote on Monday. During Friday’s session, oil  Israel from targeting Iran’s oil fields. The remarks > came a day after crude jumped more than 5% after the president seemed to suggest that the US was discussing such a > possibility with Israel. Iran produces more than three million barrels of oil a day. Interrupting supply would send prices > higher while cutting off shipments on the Straight of Hormuz, a chokepoint for crude shipments, would cause even more > upward pressure, according to analysts. \"If there's a stranglehold there, and there's a serious blockage or serious > delays, we should clear $80 [for Brent]. That is going to push oil prices significantly higher. That is a game changer,\" > Blue Line Futures founder Bill Baruch told Yahoo Finance last week. However, analysts point to spare capacity expected to > come onto the market from the Organization of the Petroleum Exporting Countries (OPEC). The oil alliance has indicated it > will start unwinding voluntary production cuts in December. Under two hypothetical scenarios where Iran's oil supply is > interrupted by either 2 million or 1 million barrels per day, Goldman Sachs sees Brent reaching a peak of $90 or the > mid-$80s, respectively, provided that OPEC rapidly offsets the shortfall. The firm predicts in the absence of major > disruptions to oil supply in the Middle East, Brent will continue to trade in the $70-$85 range, with an average price of > $77 per barrel in the fourth quarter of 2024. The possibility of interruptions from Hurricane Milton in the gulf of Mexico > has also kept crude markets uneasy. Chevron ( )   it evacuated all personnel from its Blind Faith platform in the U.S. Gulf > of Mexico and shut-in the facility in preparation for Milton. Although Florida’s west coast could see the worst winds and > rain from Milton since 2017, the inclement weather is expected to miss \"most oil and gas production platforms,\" said Bok > Financial's Kissler.",
>     "date": "2024-10-07",
>     "time": "20:19:52.000",
>     "link": "https://finance.yahoo.com/news/> oil-prices-extend-gains-as-markets-wait-for-israels-retaliation-against-iran-154717391.html"
>   },
>   {
>     "title": "Firing on All Cylinders: MRC Global (NYSE:MRC) Q2 Earnings Lead the Way",
>     "content": "Looking back on infrastructure distributors stocks’ Q2 earnings, we examine this quarter’s best and worst > performers, including MRC Global (NYSE:MRC) and its peers. Focusing on narrow product categories that can lead to economies > of scale, infrastructure distributors sell essential goods that often enjoy more predictable revenue streams. For example, > the ongoing inspection, maintenance, and replacement of pipes and water pumps are critical to a functioning society, > rendering them non-discretionary. Lately, innovation to address trends like water conservation has driven incremental > sales. But like the broader industrials sector, infrastructure distributors are also at the whim of economic cycles as > external factors like interest rates can greatly impact commercial and residential construction projects that drive demand > for infrastructure products. The 4 infrastructure distributors stocks we track reported a slower Q2. As a group, revenues > missed analysts’ consensus estimates by 1.7%. Big picture, the Federal Reserve has a dual mandate of inflation and > employment. The former had been running hot throughout 2021 and 2022 but cooled towards the central bank's 2% target as of > late. This prompted the Fed to cut its policy rate by 50bps (half a percent) in September 2024. Given recent employment > data that suggests the US economy could be wobbling, the markets will be assessing whether this rate and future cuts (the > Fed signaled more to come in 2024 and 2025) are the right moves at the right time or whether they're too little, too late > for a macro that has already cooled. Amidst this news, infrastructure distributors stocks have had a rough stretch. On > average, share prices are down 6.1% since the latest earnings results. Producing bomb casings and tracks for vehicles > during WWII, MRC (NYSE:MRC) offers pipes, valves, and fitting products for various industries. MRC Global reported revenues > of $832 million, down 4.5% year on year. This print was in line with analysts’ expectations, and overall, it was a very > strong quarter for the company with an impressive beat of analysts’ operating margin and earnings estimates. Rob Saltiel, > MRC Global’s President and CEO stated, “We achieved sequential growth in revenue, adjusted EBITDA and cash flow from > operations in the second quarter, despite slowing activity in the US oilfield and project delays in our DIET sector. We > have generated $101 million in operating cash flow through the first half of 2024, and we are tracking well to meet or > exceed our annual operating cash flow target of $200 million. MRC Global achieved the biggest analyst estimates beat but > had the slowest revenue growth of the whole group. Investor expectations, however, were likely higher than Wall Street’s > published projections, leaving some wishing for even better results (analysts’ consensus estimates are those published by > big banks and advisory firms, not the investors who make buy and sell decisions). The stock is down 2.1% since reporting > and currently trades at $12.89. Is now the time to buy MRC Global?  . Spun off from National Oilwell Varco, NOW Inc. > (NYSE:DNOW) provides distribution and supply chain solutions for the energy and industrial end markets. NOW reported > revenues of $633 million, up 6.6% year on year, in line with analysts’ expectations. The business had a strong quarter with > an impressive beat of analysts’ operating margin estimates and a decent beat of analysts’ earnings estimates. Although it > had a fine quarter compared its peers, the market seems unhappy with the results as the stock is down 9.8% since reporting. > It currently trades at $12.67. Is now the time to buy NOW?  . Formerly a division of industrial distributor HD Supply, > Core & Main (NYSE:CNM) is a provider of water, wastewater, and fire protection products and services. Core & Main reported > revenues of $1.96 billion, up 5.5% year on year, falling short of analysts’ expectations by 4.5%. It was a disappointing > quarter as it posted a miss of analysts’ earnings estimates. Core & Main delivered the weakest performance against analyst > estimates in the group. As expected, the stock is down 8.1% since the results and currently trades at $43.03. Originally a > manufacturing company, Watsco (NYSE:WSO) today only distributes air conditioning, heating, and refrigeration equipment, as > well as related parts and supplies. Watsco reported revenues of $2.14 billion, up 6.8% year on year. This number came in 2.> 1% below analysts' expectations. It was a disappointing quarter as it also recorded a miss of analysts’ same-store sales > and earnings estimates. Watsco achieved the fastest revenue growth among its peers. The stock is down 4.6% since reporting > and currently trades at $480.69. Help us make StockStory more helpful to investors like yourself. Join our paid user > research session and receive a $50 Amazon gift card for your opinions.  .",
>     "date": "2024-10-07",
>     "time": "08:18:47.000",
>     "link": "https://finance.yahoo.com/news/firing-cylinders-mrc-global-nyse-081847099.html"
>   },
> ]
> 
> ```
> 
> For each news in the json array, I want you to create 1-5 question-answer pairs based on the title and content of the news. To > create such pairs, here is some guidelines you can follow:
> 
> ===
> 1. Preprocess the Article: First, you need to preprocess the article to extract relevant information. This typically includes:
> - Splitting the article into sentences or paragraphs.
> - Identifying key entities and facts, such as people, places, dates, events, and important concepts.
> - Optionally, perform part-of-speech tagging or named entity recognition (NER) to assist in generating meaningful questions.
> 
> 2. Identify Important Information: 
> Determine the key pieces of information from the article that can be turned into questions. Some examples of important > information include:
> - Who did something? (Person-related facts)
> - What happened? (Events)
> - When did something occur? (Dates and time)
> - Where did something happen? (Places)
> - Why did something happen? (Explanations or reasons)
> - How did something happen? (Processes or sequences)
> By identifying these details, you can focus on producing questions that revolve around these key facts.
> 
> 3. Generate Questions
> Aim to generate a variety of question types:
> - Factual: "When did X happen?"
> - Definition: "What is X?"
> - Causal: "Why did X happen?"
> - Procedural: "How does X work?"
> - Inference: "What can be inferred about X?"
> 
> 4. Generate answer for each question.
> 5. Structure the output in json format like this:
> ```
> [
> 	{
> 		"link": "Link to the news that is used to create question-answer pair",
> 		"date": "Date of upload of the news used to created question-answer pair"
> 		"context": "The context used to generate question-answer pair"
> 		"question": "The question created"
> 		"answer": "The answer for the questions created".
> 	},
> 	...
> ]
> ```
> ===
> 
> Here is an example output:
> ```
> [
>     {
> 		"link": "https://finance.yahoo.com/news/market-apos-too-optimistic-apos-175752296.html?",
> 		"date": "2024-10-08",
>         "context": "Marie Curie won the Nobel Prize in Physics in 1903.",
>         "question": "When did Marie Curie win the Nobel Prize in Physics?",
>         "answer": "1903"
>     },
>     {
> 		"link": "https://finance.yahoo.com/news/mfadsfqwefsdfsa-175752296.html?",
> 		"date": "2024-10-08",
>         "context": "The capital of France is Paris.",
>         "question": "What is the capital of France?",
>         "answer": "Paris"
>     }
> ]
> ```
> 
> Only output in the format specified.

## 2. ChatGPT answer

The output json structure is:
```
[
    {
        "link": "Link to the news that is used to create question-answer pair",
        "date": "Date of upload of the news used to created question-answer pair"
        "context": "The context used to generate question-answer pair"
        "question": "The question created"
        "answer": "The answer for the questions created".
    },...
]
```

The answer from ChatGPT for the prompt above is the json below:
```
[
  {
    "link": "https://finance.yahoo.com/news/samsung-electronics-estimates-274-jump-235615435.html",
    "date": "2024-10-07",
    "context": "Samsung Electronics estimated on Tuesday a 274% jump in third-quarter operating profit but missed analyst estimates, as it struggled to capitalise on strong demand for chips used in artificial intelligence servers.",
    "question": "What percentage increase in third-quarter operating profit did Samsung Electronics estimate?",
    "answer": "274%"
  },
  {
    "link": "https://finance.yahoo.com/news/samsung-electronics-estimates-274-jump-235615435.html",
    "date": "2024-10-07",
    "context": "Samsung Electronics estimated on Tuesday a 274% jump in third-quarter operating profit but missed analyst estimates, as it struggled to capitalise on strong demand for chips used in artificial intelligence servers.",
    "question": "Why did Samsung Electronics miss analyst estimates despite the 274% increase in operating profit?",
    "answer": "It struggled to capitalise on strong demand for chips used in artificial intelligence servers."
  },
  {
    "link": "https://finance.yahoo.com/news/oil-prices-extend-gains-as-markets-wait-for-israels-retaliation-against-iran-154717391.html",
    "date": "2024-10-07",
    "context": "Oil extended its gains on Monday following its biggest weekly gain in more than a year in anticipation of an Israeli retaliation against Iran.",
    "question": "Why did oil prices extend their gains on Monday?",
    "answer": "Oil prices extended their gains due to anticipation of Israeli retaliation against Iran."
  },
  {
    "link": "https://finance.yahoo.com/news/oil-prices-extend-gains-as-markets-wait-for-israels-retaliation-against-iran-154717391.html",
    "date": "2024-10-07",
    "context": "Iran produces more than three million barrels of oil a day. Interrupting supply would send prices higher while cutting off shipments on the Straight of Hormuz would cause even more upward pressure.",
    "question": "What could happen if Iran's oil supply is interrupted?",
    "answer": "Interrupting supply would send oil prices higher and cutting off shipments on the Straight of Hormuz would cause more upward pressure."
  },
  {
    "link": "https://finance.yahoo.com/news/firing-cylinders-mrc-global-nyse-081847099.html",
    "date": "2024-10-07",
    "context": "MRC Global reported revenues of $832 million, down 4.5% year on year.",
    "question": "What were MRC Global's reported revenues for Q2 2024?",
    "answer": "$832 million."
  },
  {
    "link": "https://finance.yahoo.com/news/firing-cylinders-mrc-global-nyse-081847099.html",
    "date": "2024-10-07",
    "context": "MRC Global reported revenues of $832 million, down 4.5% year on year.",
    "question": "By what percentage did MRC Global's revenues decline year on year?",
    "answer": "4.5%."
  }
]
```
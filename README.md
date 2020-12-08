# UCLA Statistics 140SL Final Project

Made by Eustina Kim, Jennifer Lin, Ritesh Pendekanti, Diana Pham, Cassandra Tai, and Wanxin Xie

## About
For our project, we used Reddit and Twitter Sentiment as a technical indicators to predict whether a stock will be bull or bear.

## Project Poster
Our submission poster presented:
![](https://imgur.com/N3pRaA7.png)

## How to run
Follow the steps below to get files running.

### Reddit Posts
First modify the endpoint of this file to collect whichever subreddit you want the posts from.
This file will collect all posts from the past 2.5 years from the specified subreddit.
After modifying, run the following which will save the posts into a CSV file with relevant post
information as well as its sentiment using Textblob.

`python ./src/data_collection/reddit_collection/reddit_posts.py`

### Reddit Comments
Next, using the CSV generated from Reddit posts, use this file to extract all reddit comments 
from the posts. This will again collect all relevant comment information as well as its sentiment.
In order for this file to work, you will need to enter your own Reddit API key. 
Since comments do no have a character limit, to prevent this file from being too large, the CSV
does not provide the actual text of the comment. (This can take hours to run.)

`python ./src/data_collection/reddit_collection/reddit_comments.py`

### Tweets
There are two files to get Tweets. First to obtain all the tweets, use the following command:

`python ./src/data_collection/reddit_collection/twitter_comments.py`

Next to get the the sentiment of all the Tweets, use the following command:

`python ./src/data_collection/reddit_collection/sentiment_manager.py`

### Google Trends
Very simple file. Just modify name of Google Search to collect Trends from and it will return as a CSV.

`python ./src/data_collection/google_collection/google_manager.py`

### Trading Algorithm
To access the moving averages trading algorithm, use the following file:

`./src/analysis/automate_ma.R`

Use corresponding RMD file to get relevant dataframes to get function to work.

### Backtesting Algorithm
To access the backtesting trading algorithm, use the following file:

`./src/analysis/backtest_algo.R`

Use corresponding RMD file to get relevant dataframes to get function to work.

## Data Folder
Sentimental data for Apple, Disney, Intel, and Tesla can already be found in the data folder.

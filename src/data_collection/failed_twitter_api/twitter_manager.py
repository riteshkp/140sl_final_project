#!/usr/bin/env python3
# coding: utf8

import io
import csv
import json 
import requests

from twitter import Twitter, OAuth, TwitterHTTPError
from hidden import c_key, c_sec, a_tok, a_sec
from json_parser import JSONTweetParser

def error(content, *args, interrupt=False, **kwargs):
    """
    :param content: what you want to print to stderr
    :interrupt: bool that will terminate program if yes
    """
    print("\033[31m" + str(content) + "\033[0m",
          *args, file=sys.stderr, **kwargs)
    if interrupt:
        exit(-1)

def search_twitter(t, query: str, num_tweets: int):
    """
    Searches Twitter for a term and returns the data pulled from the api
    :param query: the str to be searched
    :param num_tweets: int of max number of tweets to search
    """
    # Add spaces between the query to ensure it is isolated
    query = query + ' '
    if num_tweets == 0:
        return {"statuses": []}
    try:
        raw_tweets = t.search.tweets(q=query,
                                    result_type='recent',
                                    lang='en',
                                    count=num_tweets)
    except TwitterHTTPError:
        raw_tweets = t.search.tweets(q=query,
                                    result_type='recent',
                                    lang='en',
                                    count=num_tweets)
    except Exception as err:
        print(err)
        exit(-1)
    return raw_tweets

def mine_tweet_data(t, hashtag, ticker, verbose=False, num_tweets=100000):
    """
    Mines one hashtag from twitter using the twitter api at a specified
    time and creates a file with the cleaned out tweets
    :param hashtag: str containing the hashtag that will be searched
    :param verbose: bool to toggle printing the thread and hashtag
    :param num_tweets: int of how many tweets to pull from twitter
    """
    # Search for latest tweets about the hashtag currenty selected
    try:
        raw_tweets = search_twitter(t, query=hashtag, num_tweets=num_tweets)
    except AttributeError:
        error(("attribute error"))
        exit(1)
    length = len(raw_tweets['statuses'])
    num_tweets -= length

    # Construct formatted tweet data and append it to the list of
    # clean_tweets
    clean_tweets = list()
    for index, tweet in enumerate(raw_tweets['statuses']):
        jsonParser = JSONTweetParser(raw_tweets['statuses'][index],
                                         stock=hashtag)
        clean_tweets.append(jsonParser.construct_tweet_json())

    # Search for the remainder of tweets using the coin's ticker symbol
    try:
        raw_tweets = search_twitter(t, query=ticker, num_tweets=num_tweets)
    except AttributeError:
        error(("attr error"))
        exit(1)

    length += len(raw_tweets["statuses"])
    for index, tweet in enumerate(raw_tweets['statuses']):
        jsonParser = JSONTweetParser(raw_tweets['statuses'][index], stock=hashtag)
        clean_tweets.append(jsonParser.construct_tweet_json())

    return clean_tweets

if __name__ == "__main__":
    oauth = OAuth(a_tok, a_sec, c_key, c_sec)

    # Initiate the connection to Twitter Streaming API
    try:
        t = Twitter(auth=oauth)
    except Exception as e:
        error(e)
        exit(-1)
    
    res = mine_tweet_data(t, "Tesla", "TSLA", num_tweets=100000)
    with io.open('twitter_clean_posts.csv', 'w', newline='', encoding="utf-8") as output_file:
                keys = res[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(res)
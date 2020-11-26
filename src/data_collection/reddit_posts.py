#!/usr/bin/env python3
# coding: utf8

import io
import csv
import json 
import requests
from textblob import TextBlob

def average(lst): 
    return sum(lst) / len(lst)

def calculate_sentiment(title):
    scores = list()
    blob = TextBlob(title)
    for sentence in blob.sentences:
        scores.append(sentence.sentiment.polarity)
    return average(scores)

if __name__ == "__main__":

    endpoint = 'https://api.pushshift.io/reddit/search/submission/?subreddit=amazon&sort=desc&sort_type=score&after={}d&before={}d&size=1000'
    increment = 30 # approximately each month
    end = 50

    for i in range(end):
        print(i)

        after = (i+1)*increment
        before = (i)*increment
        raw_data = requests.get(endpoint.format(after, before)).json()['data']

        relevant_data = list()

        for element in raw_data:
            try: 
                relevant_dict = {
                    'author': element['author'],
                    'created_utc': element['created_utc'],
                    'id': element['id'],
                    'num_comments': element['num_comments'],
                    'score': element['score'],
                    'subreddit': element['subreddit'],
                    'subreddit_id': element['subreddit_id'],
                    'title': element['title'],
                    'total_awards_received': element['total_awards_received'],
                    'sentiment': calculate_sentiment(element['title'])
                }
                relevant_data.append(relevant_dict)
            except:
                next

        if i == 0:
            with io.open('reddit_clean_posts.csv', 'w', newline='', encoding="utf-8") as output_file:
                keys = relevant_data[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(relevant_data)
        else:
            with io.open('reddit_clean_posts.csv', 'a', newline='', encoding="utf-8") as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writerows(relevant_data)
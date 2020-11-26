#!/usr/bin/env python3
# coding: utf8

import io
import csv
import json 
import requests
import pandas as pd
import praw

from textblob import TextBlob
from hidden import user_agent, client_id, client_secret, username, password

def average(lst): 
    return sum(lst) / len(lst)

def calculate_sentiment(title):
    scores = list()
    blob = TextBlob(title)
    for sentence in blob.sentences:
        scores.append(sentence.sentiment.polarity)
    return average(scores)

if __name__ == "__main__":
    r = praw.Reddit(user_agent=user_agent, 
                        client_id=client_id, 
                        client_secret=client_secret,
                        username=username,
                        password=password)
    ids = pd.read_csv('reddit_clean_posts.csv')['id']

    is_first = True
    for id in ids:
        submission = r.submission(id)
        submission.comments.replace_more(limit=None)
        relevant_data = list()
        for comment in submission.comments.list():
            try: 
                relevant_dict = {
                    'author': comment.author,
                    'created_utc': comment.created_utc,
                    'id': comment.id,
                    'score': comment.score,
                    'subreddit': comment.subreddit,
                    'subreddit_id': comment.subreddit_id,
                    'sentiment': calculate_sentiment(comment.body)
                }
                relevant_data.append(relevant_dict)
            except:
                next
        
        if is_first:
            with io.open('reddit_clean_comments.csv', 'w', newline='', encoding="utf-8") as output_file:
                try:
                    keys = relevant_data[0].keys()
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(relevant_data)
                    is_first = False
                except:
                    continue
        else:
            with io.open('reddit_clean_comments.csv', 'a', newline='', encoding="utf-8") as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writerows(relevant_data)
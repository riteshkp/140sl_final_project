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

    endpoint = 'https://api.twitter.com/1.1/search/tweets.json?q=%23freebandnames'
    raw_data = requests.get(endpoint).json()
    print(raw_data)

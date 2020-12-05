#!/usr/bin/env python3
# coding: utf8

import csv 
import pandas as pd
from textblob import TextBlob

def average(lst): 
    return sum(lst) / len(lst)

def calculate_sentiment(title):
    scores = list()
    blob = TextBlob(title)
    for sentence in blob.sentences:
        scores.append(sentence.sentiment.polarity)
    return average(scores)

if __name__ == '__main__':
    stocks = ["Apple", "Disney", "Intel", "Tesla"]

    for s in stocks:
        print("Computing sentiment for: ", s)

        # Read in file
        input_filepath = "data/{}_tweets.csv".format(s)
        data = pd.read_csv(input_filepath)

        # Only keep relevant rows
        relevant_cols = ["id", "date", "tweet", "likes_count", "hashtags"]
        relevant_data = data[relevant_cols]
        
        # Compute sentiment
        relevant_data["sentiment"] = relevant_data['tweet'].apply(lambda x: calculate_sentiment(x))

        # Output to CSV
        output_filepath = "data/{}_clean_tweets.csv".format(s)
        relevant_data.to_csv(output_filepath, sep=',', encoding='utf-8')
    
    print("Finished...")
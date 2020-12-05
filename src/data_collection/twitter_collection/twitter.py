#!/usr/bin/env python3
# coding: utf8

import io
import csv
import datetime
import shlex, subprocess
import twint

if __name__ == '__main__':
    stocks = ["Apple","Disney","Intel","Tesla"]

    cur_date = datetime.date(2020, 8, 3)
    end_date = datetime.date(2020, 11, 20)
    delta = datetime.timedelta(days=1)
    counter = 0

    print("Extracting Tweets")
    while cur_date <= end_date:

        if(counter % 7 == 0):
            print(str(cur_date))

        for term in stocks:

            c = twint.Config()
            c.Popular_tweets = True
            c.Min_likes = 10
            c.Search = term
            c.Since = str(cur_date)
            c.Until = str(cur_date + delta + delta)
            c.Limit = 100
            c.Store_csv = True
            c.Lang = "en"
            c.Hide_output = True
            c.Output = "data/{}_tweets.csv".format(term)
            twint.run.Search(c)

        counter += counter
        cur_date = cur_date + delta

    print("Finished")
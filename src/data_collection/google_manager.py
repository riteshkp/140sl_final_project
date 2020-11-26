#!/usr/bin/env python3
# coding: utf8

import pandas as pd
from pytrends import dailydata

if __name__ == "__main__":
    df = dailydata.get_daily_data('Disney', 2018, 1, 2020, 11, geo = '')
    compression_opts = dict(method='zip', archive_name='out.csv')  
    df.to_csv('out.zip', index=False, compression=compression_opts)  
    print(df)
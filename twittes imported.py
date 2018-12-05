# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:51:35 2018

@author: kshir
"""

import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = "wm3Y9iP9YeRVLEb93OHBm7QNK"
consumer_secret = "ii5FMEhEf54ytqifYn6mFFNYfHXKjdtdNf9D1eP4nqUR87OWAe"
access_token = "911904615578312704-VIjJCIHX3EZMNAAsL4D2CwAgeCy3Ap7"
access_token_secret = "LWcSyd6uInA7bMwt7MrSxezpsb1qh8K499kqExqrgzRQV"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------# ------ 
# Step 1: Import necessary modules and environment
# ----------------------------------------------------------------------

# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import csv

# This file contains all Twitter-related actions, so no need to import here
import zhk as tp
# ----------------------------------------------------------------------
# Step 2: Call API, get tweets, and parse tweets into a dataframe+CSV
# ----------------------------------------------------------------------

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
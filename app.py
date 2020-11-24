import tweepy
import csv
import datetime
import pandas as pd

from secrets import consumer_key, consumer_secret

# get tweets
def get_tweets(keyword, num_tweets, date):

    # auth to granting access to API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    scrappedTweets = []
    # iterate through tweets and save them to array
    for tweet in tweepy.Cursor(api.search, since=date, q=keyword).items(num_tweets):

        data = [tweet.created_at, tweet.id, tweet.geo, tweet.text, tweet.user._json['screen_name']]
        data = tuple(data)
        scrappedTweets.append(data)

    # export tweets to dataframe 
    df = pd.DataFrame(scrappedTweets, columns = ['created_at', 'tweet_id', 'geo','tweet_text', 'screen_name'])
    filename = keyword+'_scrape_'+(datetime.datetime.now().strftime("%Y-%m-%d-%H"))+'.csv'
    df.to_csv(filename, index=False)

# clean tweets
def clean_tweets(cleanTweets):
    return cleanTweets

# get sentiment
def get_sentiment(sentiment):
    return sentiment

get_tweets("rollerskating", 10, '2020-02-28')

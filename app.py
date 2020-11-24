import tweepy
import csv
import datetime

from secrets import consumer_key, consumer_secret

# get tweets
def get_tweets(keyword, num_tweets):

    # Auth API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Call API
    api = tweepy.API(auth)

    tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword).items(num_tweets):
        tweets.extend(tweet.text)

# clean tweets
def clean_tweets(cleanTweets):
    return cleanTweets

# get sentiment
def get_sentiment(sentiment):
    return sentiment

get_tweets("rollerskating", 10)

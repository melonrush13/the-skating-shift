import tweepy
import csv
import pandas as pd
import snscrape.modules.twitter as sntwitter

from secrets import consumer_key, consumer_secret

# get tweets with tweepy from the last 7 days
def get_tweets_tweepy(keyword, date):

    # auth to granting access to API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # wait_on_rate_limit is required b/c twitter has set a limit
    api = tweepy.API(auth, wait_on_rate_limit=True)

    scrapedTweets = []
    # iterate through tweets using api search and save them to array
    for tweet in tweepy.Cursor(api.search, until=date, q=keyword).items():
        data = [tweet.created_at, tweet.id, tweet.geo, tweet.text, tweet.user._json['screen_name']]
        data = tuple(data)
    
        # We only want data that doesn't have retweets
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            scrapedTweets.append(data)

    # export tweets to dataframe 
    df = pd.DataFrame(scrapedTweets, columns = ['datetime', 'tweet_id', 'geo','text', 'username'])
    filename = keyword+'_no_rt_scrape'+'.csv'
    df.to_csv(filename, index=False)

# get tweets with snscrape
def get_tweets_sn():
    snScrapedTweets = []
    # iterate through tweets using TwitterSearchScrapper and save them to array
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('rollerskates since:2020-01-01 until:2020-12-01').get_items()):
        if i>100000:
            break
        snScrapedTweets.append([tweet.date, tweet.id, tweet.content, tweet.username])

    # export tweets to dataframe
    df = pd.DataFrame(snScrapedTweets, columns = ['datetime', 'tweet_id', 'text', 'username'])
    df.to_csv('2020_rollerskates_snscrape_tweets.csv', index=False)

#get tweets using Tweepy
#get_tweets_tweepy("rollerskating", '2020-01-01')

# get tweets using sn
get_tweets_sn()

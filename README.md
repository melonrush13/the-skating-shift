# the-skating-shift

The Skating Shift is a Data Mining Project for CSCI 5502 at CU Boulder. The purpose of the project was to understand the large increase of rollerskating sales during the 2020 COVID-19 pandemic. The analysis was peformed by scraping 5 years worth of Twitter Data from keywords such as "Rollerskating", "Rollerskates", and "Rollerblades" from the years 2016 to 2020.

The data was analysized based off of trends historically, sentiment analysis, and keyword search.

## Setting Up The Project

### Dev Environment

### Development Container

Dev Containers allows users to run their development environment inside of a Docker container while using Visual Studio code. A dev container is helpful because we don't have to worry about having different versions of Python installed on our machine. Instead, we can specify what versions of everything to run inside of our Docker container and focus on our code. This is possible because of the Remote Containers VS Code Extension provided by Microsoft.

#### Requirements

- [Docker](https://www.docker.com/)
- [Remote-Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

#### Running the Container

- Press <kbd>F5</kbd> to launch the app in the container
- Press <kbd>F1</kbd> to run the Forward a port command

### Getting the Data

#### Requirements

[App.py](/Users/melanierush/Projects/CUBoulder/datamining/the-skating-shift/app.py) contains the data scraping functionality. I used two libraries to scrape Tweets: Tweepy and Snscrape. Tweepy only allowed me to scrape 7 days of historical data from their Search Index, so I instead resorted to Snscrape so I could get data from the past 5 years. Both functions are included in this python file for Tweepy and Snscrape.

- [Twitter Developer Account](https://developer.twitter.com/) Needed to gain access to Twitter API
- [Tweepy](https://www.tweepy.org/) Python library for accessing the Twitter API
- [Snscrape](https://pypi.org/project/snscrape/) Python library for scrapping large amounts of historical tweets off Twitter

## Analysis

### Analysis Set Up

I installed the following packages onto my dev container to help me with Data Analysis

- [Jupyter](https://pypi.org/project/jupyter/) Jupyter Notebooks to perform data analysis using brief Python snippits of code
- [MatPlotLib](https://pypi.org/project/matplotlib/) Used to create different visualizations based on my findings
- [Pandas](https://pypi.org/project/pandas/) Python package for data manipulation and analysis
- [Numpy](https://pypi.org/project/numpy/) Python package for operating on large multi dimensional arrays and matrices
- [TextBlob](https://pypi.org/project/textblob/) Helped me analysize sentiment from my scraped tweets with polarity and subjectivity scoring
  
### Goals

I wanted to understand the following:

- Historical patterns of Rollerskating
- Possible correlations with keywords including "COVID"
- Comparison between wheeled sports such as "Inline" and "Quad" Skating
- Sentiment of Rollerskating during 2020 and with keywords such as "COVID"

Please see my Jupyter Files for in depth Analysis
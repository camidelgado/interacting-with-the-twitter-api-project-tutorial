import os
import tweepy
import requests
import pandas as pd

consumer_key="UVBYt9C3yVLGd3vQDSgLJnMH6"
consumer_secret="NgN4liInanqCTKeYrjoLZ7XqrVcpYhKHFo8P5anXydF0xBTMyI"
access_token="1537937527910191109-SVI7UDUhdXj2Js3Mi1gkmZfW50CsZo"
access_token_secret="XlSTq8lUSsGp7mKjvAtwwZtZUWVyjXEEFOnVyUCH2To56"
bearer_token="AAAAAAAAAAAAAAAAAAAAACOGdwEAAAAAKg68UvFvZIRu6qGAKtKDbPlQwZ0%3DDQRYbNYYguBjEBj3Sj743c8gO0G9NH7x11YY7aF7Hj0HnX4h7e"

from dotenv import load_dotenv
load_dotenv()                    

import os 

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'
tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id','created_at','lang'],
                                     max_results=100)

tweets_jason=tweets.json()
print(tweets_jason)
tweets_data=tweets_jason['data']

df=pd.jason_normalize(tweets_data)
print(df)
df.to_csv('/src/data/tweets.csv')

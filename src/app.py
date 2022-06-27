import os
from dotenv import load_dotenv

import tweepy
import requests

load_dotenv()

bearer_token=os.environ.get('bearertoken')
consumer_key=os.environ.get('userkey')
consumer_secret=os.environ.get('consumersecret')
access_token=os.environ.get('keysecret')
access_token_secret=os.environ.get('accesstokensecret')

keysecret='1537937527910191109-GHnS8Y9h9xMTS40SCfKXwX3CgQ0Xij' #acceso token
userkey='qzNBsXZSBfT3l67fTSPXJBtUi' #apikey
#='2C2ahgBmLtdQRid9yZHQZdxwKkbSEEea2HO5beDmPUCpwrccom' #api key secret
bearertoken='AAAAAAAAAAAAAAAAAAAAACOGdwEAAAAAhjnDiVKS6j9jUZba4dTHcr%2F%2F6pc%3DeJ3lm2xZ2HahqB2VIoPvMmDxQ1DwwxZtsdjsSYehx8UK57qFRt' #bearer token
client=tweepy.Client(bearer_token=bearer_token,
                    consumer_key=consumer_key, 
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret,
                    return_type=requests.Response,
                    wait_on_rate_limite=True
                    )
# load the .env file variables
query='#100daysofcode (pandas OR python) -is:retweet'
tweets-client.search_recent_tweets(query=query,tweet_fields=['author_id','created_at','lang'],max_result=100)
load_dotenv()

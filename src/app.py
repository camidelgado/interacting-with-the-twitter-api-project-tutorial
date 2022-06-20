import os
from dotenv import load_dotenv

import tweepy
import requests
keysecret='1537937527910191109-GHnS8Y9h9xMTS40SCfKXwX3CgQ0Xij' #acceso token
userkey='qzNBsXZSBfT3l67fTSPXJBtUi' #apikey
#='2C2ahgBmLtdQRid9yZHQZdxwKkbSEEea2HO5beDmPUCpwrccom' #api key secret
bearertoken='AAAAAAAAAAAAAAAAAAAAACOGdwEAAAAAhjnDiVKS6j9jUZba4dTHcr%2F%2F6pc%3DeJ3lm2xZ2HahqB2VIoPvMmDxQ1DwwxZtsdjsSYehx8UK57qFRt' #bearer token
client=tweepy.Client(bearer_token=bearertoken,
                    consumer_key=userkey, 
                    consumer_secret='2C2ahgBmLtdQRid9yZHQZdxwKkbSEEea2HO5beDmPUCpwrccom',
                    access_token=keysecret,
                    access_token_secret='9hUDX9FyM5vMnGLByVmSq9dJuVRVc8xVjBVKHt5Pfk92C2' #acceso token secret
                    return_type=requests.Response,
                    wait_on_rate_limite=True
                    )
# load the .env file variables
query='#100daysofcode (pandas OR python) -is:retweet'
tweets-client.search_recent_tweets(query=query,tweet_fields=['author_id','created_at','lang'],max_result=100)
load_dotenv()

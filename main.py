import functions
import tweepy
import dotenv
import time


config = dotenv.dotenv_values(".env")

(   
    consumer_key, consumer_secret, bearer_token, access_token, 
    access_token_secret, client_id, client_secret 
) = (config[i] for i in config)

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    bearer_token=bearer_token,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# functions.reply_to_quote(client)
while True:
    time.sleep(3600)




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

auth = tweepy.OAuth1UserHandler(
       consumer_key,
       consumer_secret,
       access_token,
       access_token_secret
    )

api = tweepy.API(auth)

# functions.reply_to_quote(client)
# while True:
filename = "./img/1.png"
status = "Hello World!"
# media = api.media_upload(filename = filename)

media = api.update_status_with_media(filename = filename, status = status)

print("MEDIA: ", media)

    # tweet = api.update_status(status="Image upload", media_ids= [media.media_id_string])
    # print("TWEET: ", tweet)
    
    # client.create_tweet()
    # time.sleep(3600)




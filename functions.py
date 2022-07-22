import tweepy

def reply_to_quote(client: tweepy.Client):
    emojo = client.get_me()
    mentions = client.get_users_mentions(emojo.data.id)
    newest_tweet_id = mentions.meta['newest_id']
    client.create_tweet(in_reply_to_tweet_id=newest_tweet_id, text='teste')
    
    
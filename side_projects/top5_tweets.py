import json
import tweepy as tw
import pandas as pd

USERNAME = 'MrDeshaies'
# output options so we get more of the tweet text from pandas in the console
pd.set_option('display.width', 700)
pd.set_option('max_colwidth', 100)

def get_api_auth_token():
    with open('side_projects/twitter_api_keys.json', 'r') as f:
        api_keys = json.load(f)
    api_bearer_token = api_keys["bearer_token"]
    return api_bearer_token

def get_user_id(client, username):
    user = client.get_user(username=username)
    return user.data.id

client = tw.Client(bearer_token=get_api_auth_token())
user_id = get_user_id(client, USERNAME)

# get the tweets
tweets = tw.Paginator(client.get_users_tweets, id=user_id,
    tweet_fields=['id','public_metrics','created_at','text'],
    max_results=100).flatten(limit=5000)
tweet_data = [[tweet.id, tweet.public_metrics['like_count'], tweet.created_at, tweet.text] for tweet in tweets]

# use pandas to get the top 5
tweet_frame = pd.DataFrame(data=tweet_data, columns=['id', 'likes', 'created_at', 'text'])
tweet_frame['created_date'] = tweet_frame['created_at'].dt.date
top_5 = tweet_frame.sort_values(by='likes', ascending=False)[:5][['likes', 'created_date', 'text']]
print(top_5)
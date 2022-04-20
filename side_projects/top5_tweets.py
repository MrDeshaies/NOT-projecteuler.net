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
    exclude='retweets', max_results=100).flatten(limit=5000)
tweet_data = [[
    tweet.id, 
    tweet.public_metrics['like_count'], 
    tweet.public_metrics['retweet_count'], 
    tweet.public_metrics['quote_count'], 
    tweet.created_at, tweet.text]
    for tweet in tweets]

# use pandas to get the top 5
tweet_frame = pd.DataFrame(data=tweet_data, columns=['id', 'likes', 'retweets', 'quotes', 'created_at', 'text'])
tweet_frame['created_date'] = tweet_frame['created_at'].dt.date
tweet_frame['total_retweets'] = tweet_frame['retweets'] + tweet_frame['quotes']

print("=== Top likes ===")
top_posts = tweet_frame.sort_values(by='likes', ascending=False)[:10][['likes', 'created_date', 'text']]
print(top_posts)

print("=== Top retweets ===")
top_posts = tweet_frame.sort_values(by='total_retweets', ascending=False)[:10][['total_retweets', 'created_date', 'text']]
print(top_posts)
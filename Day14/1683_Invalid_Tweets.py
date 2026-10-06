import pandas as pd

data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

print(tweets)
invalid = []

for _, tweet in tweets.iterrows():
    if len(tweet["content"]) > 15:
        invalid.append(tweet["tweet_id"])

print(invalid)
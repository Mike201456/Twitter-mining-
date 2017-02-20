# gather data 
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
from http.client import IncompleteRead # Python 3
import time
import pandas as pd 


start = time.time()


consumer_key = 'tMJc8k8QVEYRwFbbjCqD14w5Q'
consumer_secret = 'kR4dAwSkAFrSK1IewgkwddTLeoyTquhm3ezd07TZxsIBhxQUuY'
access_token = '3330804076-g9XsAzvfwvgKYXxxlJDupKW7Jw9oawmTvdkS7OO'
access_secret = 'hUlgz2t90bBtoM40EQ9hhj83RismutJF5Lw0Xex5FhYy3'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify= True)

# gather all the new tweets with the #python hashtag
from tweepy import Stream
from tweepy.streaming import StreamListener

dates_uber= []
class MyListener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        try:
            tweet = all_data['text']
            #dates_uber.append(tweet['created_at'])
            print(tweet)
            with open('uber.json', 'a') as f:
                
                f.write(data)
            sentiment_value, confidence = s.sentiment(tweet)
            
            if confidence*100 >= 80:
                output = open('uber.txt', 'a')
                output.write(sentiment_value)
                output.write('\n')
                output.close()

        except BaseException as e:
            print("error")
            #pass
        return True
    
    def on_error(self, status):
        print(status)
        return True
#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track = ['#SuperBowl'])

while True:
    try:
        # Connect/reconnect the stream
        twitter_stream = Stream(auth, MyListener())
        # DON'T run this approach async or you'll just create a ton of streams!
        twitter_stream.filter(track = ['Uber'])
    except:
    	pass 


end = time.time()
print(end - start)
# sudo pip install tweepy

# importing the module
# http://tweepy.readthedocs.io/en/v3.5.0/api.html
import tweepy
 
# personal details - Get it from https://apps.twitter.com/
consumer_key ="xxxxxxxxxxxxxxxx" 
consumer_secret ="xxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxx"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
tweet ="Hello Everyone ! Tweeting from Python script with Media" # toDo
image_path ="/home/deve/Desktop/hi_py_tweet.png" # toDo
 
# to attach the media file
status = api.update_with_media(image_path, tweet) 
api.update_status(status = tweet)
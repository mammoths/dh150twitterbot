# MichelleBot.py 
import tweepy 
import sys 

# Consumer keys and access tokens, used for OAuth
consumer_key = 'hehe'
consumer_secret = 'dis a secret'
access_token = 'u dont get to kknow this!!'
access_token_secret = '^___^'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

robotName = 'michelleBot' 

# Get the api for a particular user 

user = api.me()
print('Starting bot with username ' + user.name + ' with ' + str(user.friends_count) + ' friends.')

# Fix for an encoding error. Basically Twitter allows characters that IDLE can't print out, so
# you have to remove the characters that lie outside of this range.
# 
# Whenever you want to print text, use .translate(non_bmp_map) on the end.
# e.g. str(myVar).translate(non_bmp_map) 

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# Just one search item for now, for #olympics hashtag.
# Can also be a username or text. 

search_results = api.search(q="#olympics", count=5)

for i in search_results:
    # Demonstrating retrieving variables from the dict, such as user.name (person who sent the
    # tweet, id (unique ID# of the tweet), and text (body of the tweet.. used to be 140, now 280).
    # 
    # Attributes should be the same as the Twitter tweet object:
    # https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    print(str(i.user.name).translate(non_bmp_map) + ' tweeted about the Olympics with the Tweet ID# ' + str(i.id) + ' and a message of ' + i.text.translate(non_bmp_map))

# From last week: 
# Access a sample method, used to update a status
# api.update_status(robotName + ' signing in for #DHCODE!')

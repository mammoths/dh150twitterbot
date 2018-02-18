#Michelle Vo
#Midterm DH150
#CareBot: tweets for friendly reminders.

import tweepy
import sys
import time
import csv
import pprint
import inspect
import random

######## SETTING UP TWEETS ########################

# Consumer keys and access tokens, used for OAuth
consumer_key = '9FQdIJSPUXYMLpNwRylPPcZP3'
consumer_secret = 'ly8sNDWzkF8mAL3IxtrILI3nMzAumqAWsmukKhWaAVZrBE0Ptb'
access_token = '963221189849006080-GABdzMfS4X7q5W9PH4BdaFBgVG3CX9z'
access_token_secret = 'XxgJS3nXfJwtnVJXCBoZrg9HSP0BNhUfyqPPsTHr4yz8c'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

robotName = 'michelleBot' 

# Get the api for a particular user 

user = api.me()


# Get the CSV files ready!
waterCSV = open('drinkwater.csv')
csvReader = csv.reader(waterCSV)
waterTweets = list(csvReader)
list_length = len(waterTweets)


#bitmap stuff
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#tweets I've seen before!
viewedTweets = {}

################ CODE MAGIC #####################

def postTweet(tweet):
   api.update_status(tweet)
   print(tweet)

#posts general reminder about drinking water
def postGeneralTweet(index):
   tweet = str(waterTweets[index][0]).translate(non_bmp_map)
   postTweet(tweet)

def HaveISeenThisTweetBefore(user_id):
   if (user_id in viewedTweets):
      return True
   else:
      viewedTweets.update({user_id:1})
      return False
      



#responds to users a general 
def respondTweet():
   print ("checking my dms!") 
   wrote_to_me = api.search(q='@' + str(user.screen_name), count=20)
   for i in wrote_to_me:
      if (i.user.screen_name != user.screen_name):
         if (HaveISeenThisTweetBefore(str(i.id)) == False):
            fan = str(i.user.screen_name).translate(non_bmp_map)
            fanTweet = 'hello @' + fan + '! have a nice day!!' 
            postTweet(fanTweet)
      

   
  


############### TURN BOT ON ###################

def main():

   halfchance = 0
   counter = 0
   while (counter < list_length):
        respondTweet()
        if (halfchance % 2 == 0):
           postGeneralTweet(counter)
           counter = counter + 1
        halfchance = random.randint
        time.sleep(500) #for now, but eventually it'll be once every 5 min. 


if __name__ == "__main__":
    main()

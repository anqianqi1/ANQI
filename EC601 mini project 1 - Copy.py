#!/usr/bin/env python

# Author - anqiguo


from tweepy import OAuthHandler, API
import wget

# Twitter API credentials
consumer_key = "Enter the consumer_key"
consumer_secret = "Enter the consumer_secret"
access_key = "Enter the access_key"
access_secret = "Enter the access_secret"


def get_image():

    # authorize twitter, initialize tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = API(auth)


    "media_url": "https://twitter.com/BU_Tweets.jpg"


        wget.download("media_url",'C:\Users\anqia\Documents\SCHOOL\2018 FALL\EC 601 product design\mini assingment 1')
    }


    print('done')





if __name__ == '__main__':
    get_image()

   

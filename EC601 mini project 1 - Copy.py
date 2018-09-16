#!/usr/bin/env python

# Author - anqiguo


from tweepy import OAuthHandler, API
import wget

# Twitter API credentials
consumer_key = "jTC38AzwtgHKzLvusvOHm1ni4"
consumer_secret = "H1WnO5q4oIq0VRs9coqJ5BjSmkIcx2DEhoXBOz77JaI7k0wboJ"
access_key = "1039258380504846341-VzdOeFASNH5Kr2DSqLTtg7yIfIVEVy"
access_secret = "Fcwy6ArMGLJoIrEZUOT4Rp4J8E36FOt6nNPUF5NABEBWh"


def get_image():

    # authorize twitter, initialize tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = API(auth)

    "media":[
    {
    "media_url": "https://twitter.com/BU_Tweets.jpg"


        wget.download("media_url",'C:\Users\anqia\Documents\SCHOOL\2018 FALL\EC 601 product design\mini assingment 1')
    }
    ]

    print('done')


def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'C:\Users\anqia\Documents\SCHOOL\2018 FALL\EC 601 product design\mini assingment 1') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)



def ffmpeg()
    ffmpeg -i image2 -framerate 12 -i foo-%03d.fpeg -s Wxh foo.avi



if __name__ == '__main__':
    get_image()

    google_vision()

    ffmpeg()


   

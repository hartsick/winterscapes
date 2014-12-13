import os
from twython import Twython

class Tweeter(Twython):
    def __init__(self, *args, **kwargs):
        self.twitter = Twython(*credentials())

    def credentials():
      consumer_key = os.environ.get('CHRISTMASSCAPE_CONSUMER_KEY')
      consumer_secret = os.environ.get('CHRISTMASSCAPE_CONSUMER_SECRET')
      access_token = os.environ.get('CHRISTMASSCAPE_ACCESS_TOKEN')
      access_token_secret = os.environ.get('CHRISTMASSCAPE_ACCESS_TOKEN_SECRET')

      credentials = (   consumer_key,
                        consumer_secret,
                        access_token,
                        access_token_secret)

      return credentials

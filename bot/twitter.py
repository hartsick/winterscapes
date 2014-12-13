import os

class Tweeter(object):
    def __init__(self, twitter_api):
        self.twitter = twitter_api(*self.credentials())

    def credentials(self):
      consumer_key = os.environ.get('CHRISTMASSCAPE_CONSUMER_KEY')
      consumer_secret = os.environ.get('CHRISTMASSCAPE_CONSUMER_SECRET')
      access_token = os.environ.get('CHRISTMASSCAPE_ACCESS_TOKEN')
      access_token_secret = os.environ.get('CHRISTMASSCAPE_ACCESS_TOKEN_SECRET')

      credentials = (   consumer_key,
                        consumer_secret,
                        access_token,
                        access_token_secret)

      return credentials

    def tweet(self, tweet):
        self.twitter.update_status(status=tweet)

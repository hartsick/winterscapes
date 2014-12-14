from twython import Twython
from bot.twitter import Tweeter
from bot.tweet_gen import WinterscapeGenerator

twitter = Tweeter(Twython)
tweet = WinterscapeGenerator().generate_tweet()

twitter.tweet(tweet)

# def run_stream():
#     # Run tweets four times daily during work hours
#     while True:
#         try:
#             stream = TweetStreamer(*twitter_credentials_init())
#             stream.user(**{'with': 'user'})
#         except Exception as e:
#             logging.exception(e)

#         time.sleep(60)

# 7am
# 10am
# 2pm
# 5pm

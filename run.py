from twython import Twython
from bot.twitter import Tweeter
from bot.tweet_gen import WinterscapeGenerator

twitter = Tweeter(Twython)
tweet = WinterscapeGenerator().generate_tweet()

twitter.tweet(tweet)

from twython import Twython
from bot.twitter import Tweeter
from bot.tweet_gen import WinterscapeGenerator
from datetime import datetime

def run_bot():

    # Run tweets four-ish times daily during work hours
    while True:

        current_hour = datetime.now().hour
        if current_hour => 7 and current_hour <= 19:
            try:
                twitter = Tweeter(Twython)
                tweet = WinterscapeGenerator().generate_tweet()
                twitter.tweet(tweet)

            except Exception as e:
                logging.exception(e)

            # tweet again in three hours
            time.sleep(10800)

        else:
            # check again in an hour
            sleep(3600)

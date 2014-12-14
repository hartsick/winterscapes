from twython import Twython
from bot.twitter import Tweeter
from bot.tweet_gen import WinterscapeGenerator
from datetime import datetime
import time

def run_bot():

    # Run tweets four-ish times daily during work hours
    while True:

        current_hour = datetime.now().hour
        if current_hour >= 7 and current_hour <= 19:
            try:
                twitter = Tweeter(Twython)
                tweet = WinterscapeGenerator().generate_tweet()
                twitter.tweet(tweet)

                # tweet again in three hours
                time.sleep(10800)
            except Exception as e:
                logging.exception(e)


        else:
            # check again in an hour
            time.sleep(3600)


if __name__ == "__main__":

    run_bot()

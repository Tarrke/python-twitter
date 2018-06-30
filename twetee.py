#!/usr/bin/env python3

import tweepy
import time

from twitter_secure import *

def tweeter_login():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token_key, token_secret)
    api = tweepy.API(auth)
    return api

def tweet(api, message):
    api.update_status(status=message)

def search_and_print(api, q):
    statuses = api.search(q)

    statuses = api.user_timeline(id = user.id, count = 200)
    for status in statuses:
        print("***")
        print("By", status.user.screen_name)
        print(status.text)
        print("Retweet count:", str(status.retweet_count))
        print("Favorite count:", str(status.favorite_count))
        print(status.created_at)
        time.sleep(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Just a little twitter helper")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--search", help="Keyword for search")
    group.add_argument("-m", "--message-send", help="The message to send")
    args = parser.parse_args()

    api = tweeter_login()
    user = api.get_user('Tarrke')

    # No options called:
    has_arg = False
    if args.search:
        search_and_print(api, args.search)
    elif args.message_send:
        tweet(api, args.message_send)
    else:
        parser.print_help()
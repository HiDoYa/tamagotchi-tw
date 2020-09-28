#!/usr/bin/python3
import sys
import os
import random
import tweepy

if len(sys.argv) != 2:
    print("Usage: ./tweet.py /path/to/dir")
    exit()

access_token = os.environ['TW_ACCESS_TOKEN']
access_token_secret = os.environ['TW_ACCESS_TOKEN_SECRET']
consumer_key = os.environ['TW_API_KEY']
consumer_key_secret = os.environ['TW_API_KEY_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
tw = tweepy.API(auth)

ls = os.listdir(os.path.join(sys.argv[1], "tama_images"))
selected_im = random.choice(ls)

im_handler = tw.media_upload(os.path.join(sys.argv[1],"tama_images/", selected_im))
media_ids = [im_handler.media_id_string]
status = tw.update_status("Today's tamagotchi!", media_ids=media_ids, source="random user")

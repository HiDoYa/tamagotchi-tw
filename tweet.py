#!/usr/bin/python3
import pathlib
import os
import random
import tweepy

access_token = os.environ['TW_ACCESS_TOKEN']
access_token_secret = os.environ['TW_ACCESS_TOKEN_SECRET']
consumer_key = os.environ['TW_API_KEY']
consumer_key_secret = os.environ['TW_API_KEY_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
tw = tweepy.API(auth)

parent_path = str(pathlib.Path(__file__).parent.resolve())

ls = os.listdir(os.path.join(parent_path, "tama_images"))
selected_im = random.choice(ls)

im_handler = tw.media_upload(os.path.join(parent_path, "tama_images/", selected_im))
media_ids = [im_handler.media_id_string]
status = tw.update_status("Today's tamagotchi!", media_ids=media_ids, source="random user")

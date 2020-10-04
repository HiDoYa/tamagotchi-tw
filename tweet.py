#!/usr/bin/python3
import pathlib
import os
import random
import tweepy

def get_name(im):
    jp_name = ""
    en_name = ""
    im = im.replace("jpg", "txt")
    parent_path = str(pathlib.Path(__file__).parent.resolve())
    jp_dir = os.path.join(parent_path, "name_tama_images_meta_jp")
    en_dir = os.path.join(parent_path, "name_tama_images_meta_en")
    with open(os.path.join(jp_dir, im), "r") as f:
        jp_name = f.read()

    with open(os.path.join(en_dir, im), "r") as f:
        en_name = f.read()

    return jp_name, en_name

access_token = os.environ['TW_ACCESS_TOKEN']
access_token_secret = os.environ['TW_ACCESS_TOKEN_SECRET']
consumer_key = os.environ['TW_API_KEY']
consumer_key_secret = os.environ['TW_API_KEY_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
tw = tweepy.API(auth)

parent_path = str(pathlib.Path(__file__).parent.resolve())

ls = os.listdir(os.path.join(parent_path, "imag_tama_images"))
selected_im = random.choice(ls)

jp_name, en_name = get_name(selected_im)
im_handler1 = tw.media_upload(os.path.join(parent_path, "imag_tama_images/", selected_im))
im_handler2 = tw.media_upload(os.path.join(parent_path, "tama_images/", selected_im))
media_ids = [im_handler1.media_id_string, im_handler2.media_id_string]
status = tw.update_status("Today's tamagotchi!: {} / {}".format(jp_name, en_name), media_ids=media_ids, source="random user")

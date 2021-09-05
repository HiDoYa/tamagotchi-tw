#!/usr/bin/python3
import os
import random
import tweepy
import boto3

## Note: Files must be downloaded to /tmp due to Lambda limitation (only tmp is writable)

def get_name():
    jp_file = "/tmp/name_tama_images_meta_jp.txt"
    en_file = "/tmp/name_tama_images_meta_en.txt"

    jp_name = open(jp_file, "r").read()
    en_name = open(en_file, "r").read()

    return jp_name, en_name

def auth_tweepy():
    access_token = os.environ['TW_ACCESS_TOKEN']
    access_token_secret = os.environ['TW_ACCESS_TOKEN_SECRET']
    consumer_key = os.environ['TW_API_KEY']
    consumer_key_secret = os.environ['TW_API_KEY_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    tw = tweepy.API(auth)

    return tw

def tweet(tw):
    jp_name, en_name = get_name()
    im_handler1 = tw.media_upload("/tmp/imag_tama_images.jpg")
    im_handler2 = tw.media_upload("/tmp/tama_images.jpg")
    media_ids = [im_handler1.media_id_string, im_handler2.media_id_string]
    message = "Today's tamagotchi!: {} / {}".format(jp_name, en_name)

    status = tw.update_status(message, media_ids=media_ids, source="random user")
    print("Tweet status", status)

def get_locs(folder, chosen_obj, suffix):
    s3_loc = "{}/{}{}".format(folder, chosen_obj, suffix)
    lambda_loc = "/tmp/{}{}".format(folder, suffix)
    return s3_loc, lambda_loc

def choose_random(bucket):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    ls = []
    for obj in bucket.objects.filter(Prefix="imag_tama_images/"):
        ls.append(obj.key)
    chosen_obj = random.choice(ls)
    chosen_obj = chosen_obj.removeprefix("imag_tama_images/")
    chosen_obj = chosen_obj.removesuffix(".jpg")
    return chosen_obj

def lambda_main(event, context):
    print("Choosing random image")
    bucket = "tamagotchi-files"
    chosen_obj = choose_random(bucket)
    print("Chosen: ", chosen_obj)

    print("Downloading files")
    s3_client = boto3.client('s3')
    for x in ["imag_tama_images", "tama_images"]:
        s3_loc, lambda_loc = get_locs(x, chosen_obj, ".jpg")
        print("Downloading", s3_loc, "to", lambda_loc)
        s3_client.download_file(bucket, s3_loc, lambda_loc)

    for x in ["name_tama_images_meta_en", "name_tama_images_meta_jp"]:
        s3_loc, lambda_loc = get_locs(x, chosen_obj, ".txt")
        print("Downloading", s3_loc, "to", lambda_loc)
        s3_client.download_file(bucket, s3_loc, lambda_loc)

    print("Authenticating tweepy")
    tw = auth_tweepy()

    print("Making tweet")
    tweet(tw)

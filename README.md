# Tamagotchi Tweeter

Tweets random tamagotchi image everyday at [twitter link](https://twitter.com/Tamagocchi15). Tamagotchi images are scraped from the official tamagotchi website. Tamaogotchi names are then parsed from the images via Google Cloud OCR (after preprocessing with python pillow) and is translated to English through Google Cloud Translate service. Currently deployed on aws ec2 instance.

![Screenshot preview](preview.png)


## Architecture
The tamagotchi images and descriptions are stored in S3. An AWS lambda is run on a schedule to choose a random tamagotchi image and post it on twitter.

This project uses terraform to manage the AWS resources.

## Running Instructions
### Version 3 (current)
Set the following environment variables with your twitter API keys: ```TF_VAR_TW_API_KEY, TF_VAR_TW_API_KEY_SECRET, TF_VAR_TW_ACCESS_TOKEN, TW_FAR_TW_ACCESS_TOKEN_SECRET```.

Run make in the root directory. If this is your first run, you must also be logged into aws cli as well as ```terraform init``` in the terraform/ directory.

### Version 2
To run on server, first create a secrets.env file in the base directory with all twitter keys: ```TW_API_KEY, TW_API_KEY_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET```. Get these variables from twitter API dashboard.

Make sure to run the utility shell script to download all tamagotchi images and load them in (instructions below). Then, run the provided startup script to create the cron job which runs the tweet.py script to tweet tamagotchi characters at 12:00 PM everyday.

### Version 1
AWS\_rds with MYSQL was also utilized to store all tamagotchi character metadata, but was switched to simple file storage due to expensive costs.


## Utility
Scrapes and downloads all tamagotchi image files, then cuts them so that miscellaneous text is cut out. This is a one time operation so it need not be repeated again. All these files are stored in a S3 bucket.

Run ```./run.sh create``` to create correct.txt file which contains Japanese and English tamaogtchi names. Correct these names (there may be some error due to imperfect OCR). 

Then, run ```./run.sh load``` to load in the corrected file and setup images/names for tweeting.
Note: cpy_crrect.txt contains the currently corrected Japanese and English names. This may be further corrected in the future.

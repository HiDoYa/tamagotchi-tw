# Tamagotchi Tweeter

Tweets random tamagotchi image everyday at twitter.com/Tamagocchi15. Tamagotchi images scraped used separate utility from official tamagotchi website. Tamaogotchi names are parsed from the images via Google Cloud OCR (after preprocessing with python pillow) and is translated to English through Google Cloud Translate service. Currently deployed on aws ec2 instance.

Aws\_rds with MYSQL was also utilized to store all tamagotvhi character metadata, but was switched to simple file storage due to expensive costs.

To run on server, first create a secrets.env file in the base directory with all twitter keys: ```TW_API_KEY, TW_API_KEY_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET```. Get these variables from twitter API dashboard.

Make sure to run the utility shell script to download all tamagotchi images and load them in (instructions below). Then, run the provided startup script to create the cron job which runs the tweet.py script to tweet tamagotchi characters at 12:00 PM everyday.

## Utility
Scrapes and downloads all tamagotchi image files, then cuts them so that miscellaneous text is cut out.
Run ```./run.sh create``` to create correct.txt file which contains Japanese and English tamaogtchi names. Correct these names (there may be some error due to imperfect OCR). Then, run ```./run.sh load``` to load in the corrected file and setup images/names for tweeting.
Note: cpy_crrect.txt contains the currently corrected Japanese and English names. This may be further corrected in the future.

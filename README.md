# Tamagotchi Tweeter

Tweets random tamagotchi image everyday at twitter.com/Tamagocchi15. Tamagotchi images scraped used separate utility from official tamagotchi website. Currently deployed on aws ec2 instance.

To run on server, first create a secrets.env file in the base directory with all twitter keys: ```TW_API_KEY, TW_API_KEY_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET```. Get these variables from twitter API dashboard.

Make sure to run the utility shell script to download all tamagotchi images and place them in a directory called "tama\_images" in the base directory. Then, run the provided startup script to create the cron job.

## Utility
Scrapes and downloads all tamagotchi image files, then cuts them so that miscellaneous text is cut out.

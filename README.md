# Tamagotchi Tweeter

Tweets random tamagotchi image everyday at twitter.com/Tamagocchi15. Tamagotchi images scraped used separate utility from official tamagotchi website. Currently deployed on aws ec2 instance.

To run on server, first create secrets file with all twitter keys, and load in with your shell (e.g. put keys in a secrets.env file and load in the .env file in bash\_profile). You must create environment variables: ```TW_API_KEY, TW_API_KEY_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET```. Get these variables from twitter API dashboard.

Make sure to run the utility shell script to download all tamagotchi images and place them in a directory called "tama\_images" in the base directory. Then change permissions for tweet.py:
```
chmod +x tweet.py
```

Then, create cron job to run tweet.py every day with
```
0 12 * * * /path/to/tweet.py
```

## Utility
Scrapes and downloads all tamagotchi image files. May need to be manually sorted to check for invalid images. (I know, I shouldn't be using c++ for this. I'm reusing old code.) 

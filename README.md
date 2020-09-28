# Tamagotchi Tweeter

Tweets random tamagotchi image everyday at twitter.com/Tamagocchi15. Tamagotchi images scraped used separate utility from official tamagotchi website. Currently deployed on aws ec2 instance.

To run on server, first create secrets file with all twitter keys, and load in with your shell. Then:
```
chmod +x tweet.py
```

Then, create cron job to run tweet.py every day with
```
0 12 * * * /path/to/tweet.py
```

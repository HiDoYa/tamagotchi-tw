# Tamagotchi Tweeter

Tweets random tamagotchi image everyday at https://twitter.com/Tamagocchi15. Tamagotchi images scraped used separate utility from official tamagotchi website. 

To run on server, first install secrets file with all twitter keys.
```
source secrets.env
```

Then, create cron job to run tweet.py every day with
```
0 12 * * * /path/to/tweet.py
```

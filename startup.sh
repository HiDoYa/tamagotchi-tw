#!/bin/bash
chmod +x tweet.py

# Save current cron jobs, append our cronjob
crontab -l > tempcron
echo "0 12 * * * source $HOME/tamagotchi_tw/secrets.env; $HOME/tamagotchi_tw/tweet.py >> $HOME/log.txt 2>&1" >> tempcron
crontab tempcron
rm tempcron

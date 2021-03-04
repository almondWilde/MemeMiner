#write out current crontab
#crontab -l > mycron
#echo new cron into cron file
#echo "02 00 * * * echo hello" >> mycron
#install new cron file
#crontab mycron
#rm mycron

#write out current crontab
crontab -l > mememiner.cron
#echo new cron into cron file
echo "*/2 00 * * * mine.sh" >> mememiner.cron
#install new cron file
crontab mememiner.cron
rm mememiner.cron

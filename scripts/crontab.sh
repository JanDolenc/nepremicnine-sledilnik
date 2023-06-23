# Scrape by region

# Day 1 - gorenjska
# Stanovanje
0 17 1,6,11,16,21,26 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh gorenjska stanovanje >> /home/nepremicnine-sledilnik/logs/cron-job/cron-gorenjska-s-`date +\%y-\%m-\%d`.log 2>&1

# Hisa
0 6 1,6,11,16,21,26 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh gorenjska hisa >> /home/nepremicnine-sledilnik/logs/cron-job/cron-gorenjska-h-`date +\%y-\%m-\%d`.log 2>&1


# Day 2 - lj mesto
# Stanovanje
0 10 2,7,12,17,22,27 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh ljubljana-mesto stanovanje >> /home/nepremicnine-sledilnik/logs/cron-job/cron-lj-mesto-s-`date +\%y-\%m-\%d`.log 2>&1

# Hisa
0 17 2,7,12,17,22,27 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh ljubljana-mesto hisa >> /home/nepremicnine-sledilnik/logs/cron-job/cron-lj-mesto-h-`date +\%y-\%m-\%d`.log 2>&1


# Day 3 - južna primorska
# Stanovanje
0 6 3,8,13,18,23,28 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh juzna-primorska stanovanje >> /home/nepremicnine-sledilnik/logs/cron-job/cron-j-primorska-s-`date +\%y-\%m-\%d`.log 2>&1

# Hisa
0 10 3,8,13,18,23,28 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh juzna-primorska hisa >> /home/nepremicnine-sledilnik/logs/cron-job/cron-j-primorska-h-`date +\%y-\%m-\%d`.log 2>&1


# Day 4 - podravska
# Stanovanje
0 6 4,9,14,19,24,29 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh podravska stanovanje >> /home/nepremicnine-sledilnik/logs/cron-job/cron-podravska-s-`date +\%y-\%m-\%d`.log 2>&1

# Hisa
0 17 4,9,14,19,24,29 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh podravska hisa >> /home/nepremicnine-sledilnik/logs/cron-job/cron-podravska-h-`date +\%y-\%m-\%d`.log 2>&1


# Day 5 - lj okolica
# Stanovanje
0 6 5,10,15,20,25,30 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh ljubljana-okolica stanovanje >> /home/nepremicnine-sledilnik/logs/cron-job/cron-lj-okolica-s-`date +\%y-\%m-\%d`.log 2>&1

# Hisa
0 10 5,10,15,20,25,30 * * /bin/bash /home/nepremicnine-sledilnik/scripts/cron-job-crawler.sh ljubljana-okolica hisa >> /home/nepremicnine-sledilnik/logs/cron-job/cron-lj-okolica-h-`date +\%y-\%m-\%d`.log 2>&1

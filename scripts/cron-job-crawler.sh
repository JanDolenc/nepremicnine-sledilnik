#!/bin/bash

# Arguments needed
# $1 - regija
# $2 - vrsta | stanovanje / hisa
# Command line: /path/to/script.sh gorenjska hisa

# Set acronym for regija based on $1 argument
if [ "$1" = "ljubljana-okolica" ]; then
    regija_acronym="lj-okolica"
elif [ "$1" = "ljubljana-mesto" ]; then
    regija_acronym="lj-mesto"
elif [ "$1" = "juzna-primorska" ]; then
    regija_acronym="j-primorska"
else
    regija_acronym=$1
fi


# Set acronym for vrsta based on $2 argument
if [ "$2" = "stanovanje" ]; then
  vrsta_acronym="s"
fi
if [ "$2" = "hisa" ]; then
  vrsta_acronym="h"
fi


echo "----------------------------"
echo "CRON JOB $(basename $BASH_SOURCE) STARTED!"
echo "Date time is: $(date)"
echo "----------------------------"


echo "Regija:${1}"
echo "Okrajšava: ${regija_acronym}"
echo "Vrsta:${2}"
echo "Okrajšava: ${vrsta_acronym}"


# Step 1 - sleep for random x seconds 3 - 14400
echo " "
echo "Sleep"
echo "----------------------------"

# Generate a random sleep time between 3 and 14400 seconds
# POPRAVI - nastavi čas na 1440
sleep_time=$(shuf -i 3-14400 -n 1)
sleep_time_min=$(expr ${sleep_time} / 60)
echo "Sleeping for ${sleep_time} seconds | ${sleep_time_min} min"
sleep "${sleep_time}s"

echo "---"
echo "Woke up at: $(date)" 
echo "Going to work!"


# Step 2 - Setup wiregurad
echo " "
echo "Setup Wireguard"
echo "----------------------------"

# Step 2a - Select random config
# Define an array of strings
wg_configs=("wg0" "wg2" "wg3" "wg4" "wg5")
# Configs for testing
#wg_configs=("wg5" "wg5")

# Generate a random index into the array
random_index=$(shuf -i 0-$((${#wg_configs[@]}-1)) -n 1)

# Get the value at the random index
random_config=${wg_configs[$random_index]}

# Print the random string
echo "Using config: ${random_config}"

echo "---"

# Step 2b - run wg-quick up
cd /etc/wireguard

sudo wg-quick up "${random_config}"

echo "---"

echo "Using these wireguard settings:" 

wg show


# Step 3 - Setup docker
echo " "
echo "Setup Docker"
echo "----------------------------"

cd /home/nepremicnine-sledilnik/crawler

# Start the containers
docker compose --env-file ./../.env up -d  

# Wait for the containers to start up
while [ "$(docker ps | grep crawler | awk '{print $7}')" != "Up" ]; do
    echo "NOT JET"
    sleep 1
done

echo "READYYYY"

# Logs from flaresolverr container output into a file
docker logs -f flaresolverr &> /home/nepremicnine-sledilnik/logs/flaresolverr/flare-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").log &

# Step 4 - Run crawler 
echo " "
echo "Run crawler"
echo "----------------------------"

echo "Crawler start at: $(date)"

echo "Scraping | regija: $1 | vrsta: $2"

docker exec crawler scrapy crawl nepremicninespider -a regija=$1 -a vrsta=$2 -O scraped-data/data-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").json -s LOG_FILE=logs/scrapy-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").log

echo "Crawler finished at: $(date)"


# Step 5 - Copy files Docker -> host 
echo " "
echo "Copy files Docker -> host"
echo "----------------------------"

# Copy data - json file
docker cp crawler:/usr/src/crawler/scraped-data/data-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").json /home/nepremicnine-sledilnik/crawler/scraped-data-host

# Copy log file
docker cp crawler:/usr/src/crawler/logs/scrapy-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").log /home/nepremicnine-sledilnik/logs/scrapy


# Step 6 - Close docker - remove containers 
echo " "
echo "Docker down"
echo "----------------------------"

docker compose --env-file ./../.env down 

echo "Done - containers removed"


# Step 7 - Stop wireguard
echo " "
echo "Stop wireguard"
echo "----------------------------"

cd /etc/wireguard

sudo wg-quick down "${random_config}"

wg show

echo "---"

echo "Wireguard is switched off"


# Finish
echo ""
echo "Job is finished! Time: $(date)"

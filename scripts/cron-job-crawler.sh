#!/bin/bash

# FLAGS
# Defaults
regija=""
vrsta=""
sleep=""
wg=""
my_path="/home"

# Set flags
while getopts r:v:s:w:p: flag
do
   case "${flag}" in
      r) regija=${OPTARG};;
      v) vrsta=${OPTARG};;
      s) sleep=${OPTARG};;
      w) wg=${OPTARG};;
      p) my_path=${OPTARG};;
   esac
done

# Required flags
# r - regija
# v - vrsta
# Optional flags
# s - sleep - default empty or true - sleep for random up to 4 hours
# w - wg - default empty or true / on
# p - path default is /home if not set otherwise
# Command line: /path/to/script.sh -r gorenjska -v hisa -s no-sleep -w wg-off -p /custom/path

# Set acronym for regija based on $regija argument
if [ "$regija" = "ljubljana-okolica" ]; then
    regija_acronym="lj-okolica"
elif [ "$regija" = "ljubljana-mesto" ]; then
    regija_acronym="lj-mesto"
elif [ "$regija" = "juzna-primorska" ]; then
    regija_acronym="j-primorska"
else
    regija_acronym=$regija
fi


# Set acronym for vrsta based on $vrsta argument
if [ "$vrsta" = "stanovanje" ]; then
  vrsta_acronym="s"
fi
if [ "$vrsta" = "hisa" ]; then
  vrsta_acronym="h"
fi


echo "----------------------------"
echo "CRON JOB $(basename $BASH_SOURCE) STARTED!"
echo "Date time is: $(date)"
echo "----------------------------"


echo "Regija:${regija}"
echo "Okrajšava: ${regija_acronym}"
echo "Vrsta:${vrsta}"
echo "Okrajšava: ${vrsta_acronym}"
echo "sleep: $sleep";
echo "wg: $wg";
echo "my-path: $my_path";


# Step 1 - sleep for random x seconds 3 - 14400
echo " "
echo "Sleep"
echo "----------------------------"
if [ "$sleep" = "no-sleep" ]; then

    echo "Skipping sleep. Going to work!"
    
else
    # Generate a random sleep time between 3 and 14400 seconds
    sleep_time=$(shuf -i 3-14400 -n 1)
    sleep_time_min=$(expr ${sleep_time} / 60)
    echo "Sleeping for ${sleep_time} seconds | ${sleep_time_min} min"
    sleep "${sleep_time}s"

    echo "---"
    echo "Woke up at: $(date)" 
    echo "Going to work!"
fi


# Step 2 - Setup wiregurad
echo " "
echo "Setup Wireguard"
echo "----------------------------"
if [ "$wg" = "wg-off" ]; then

    echo "Wireguard is off/disabled."
    
else
    # Step 2a - Select random config
    # Define an array of strings
    wg_configs=("wg1" "wg2" "wg3" "wg5" "wg6" "wg7" "wg8" "wg9" "wg10" "wg11" "wg12")
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
fi


# Step 3 - Setup docker
echo " "
echo "Setup Docker"
echo "----------------------------"

# Select which flaresolverr version to use
flare_versions=("v3.2.1" "v3.2.0" "v3.1.2" "v3.1.1" )

# Generate a random index into the array
random_index_flare=$(shuf -i 0-$((${#flare_versions[@]}-1)) -n 1)

# Get the value at the random index
random_version=${flare_versions[$random_index_flare]}

# Set variable with new random version in .env file
cd ${my_path}/nepremicnine-sledilnik

sed -i "s/FLARESOLVERR_VERSION=.*/FLARESOLVERR_VERSION=${random_version}/g" .env

echo "Using flaresolverr version: ${random_version}"

# Start the containers
cd ${my_path}/nepremicnine-sledilnik/crawler

docker compose --env-file ./../.env up -d

# Wait for the containers to start up
while [ "$(docker ps | grep crawler | awk '{print $7}')" != "Up" ]; do
    echo "NOT JET"
    sleep 1
done

echo "READYYYY"

# Logs from flaresolverr container output into a file
docker logs -f flaresolverr &> ${my_path}/nepremicnine-sledilnik/logs/flaresolverr/flare-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").log &


# Step 4 - Run crawler 
echo " "
echo "Run crawler"
echo "----------------------------"

echo "Crawler start at: $(date)"

echo "Scraping | regija: $regija | vrsta: $vrsta"

docker exec crawler scrapy crawl nepremicninespider -a regija=$regija -a vrsta=$vrsta -O data-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").json -s LOG_FILE=scrapy-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").log

echo "Crawler finished at: $(date)"


# Step 5 - Copy files Docker -> host 
echo " "
echo "Copy files Docker -> host"
echo "----------------------------"

# Copy data - json file
docker cp crawler:/usr/src/crawler/data-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").json ${my_path}/nepremicnine-sledilnik/crawler/scraped-data-host

# Copy log file
docker cp crawler:/usr/src/crawler/scrapy-${regija_acronym}-${vrsta_acronym}-$(date +"%y-%m-%d").log ${my_path}/nepremicnine-sledilnik/logs/scrapy


# Step 6 - Close docker - remove containers 
echo " "
echo "Docker down"
echo "----------------------------"

docker compose --env-file ./../.env down 

echo "Done - containers removed"


# Step 7 - Stop wireguard
if [ "$wg" != "wg-off" ]; then
    echo " "
    echo "Stop wireguard"
    echo "----------------------------"

    cd /etc/wireguard

    sudo wg-quick down "${random_config}"

    wg show

    echo "---"

    echo "Wireguard is switched off"
fi


echo " "
echo "Job summary"
echo "----------------------------"
echo "Regija:${regija}"
echo "Vrsta:${vrsta}"
echo "Wg config: ${random_config}"
echo "Flaresolverr version: ${random_version}"

# Finish
echo ""
echo "Job is finished! Time: $(date)"

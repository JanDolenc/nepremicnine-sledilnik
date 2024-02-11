#!/bin/bash

# 1. MOVE FILES INTO IMPORTER DIR
echo "Date time is: $(date)"
echo ""

src_dir="/home/nepremicnine-sledilnik/crawler/scraped-data-host"
dest_dir="/home/nepremicnine-sledilnik/database/importer/import-data"

count=0
# Use a for loop to iterate over the files in the source directory
for file in "$src_dir"/*; do
    # Check if the item is a file (not a directory)
    if [[ -f $file ]]; then
        # Increment the counter
        ((count++))
        # Move the file to the destination directory
        mv "$file" "$dest_dir/"
        echo "moving $file"
        # Break the loop once we've moved  20 files
        if [[ $count -eq  25 ]]; then
            break
        fi
    fi
done

echo ""
echo "Moved $count files from $src_dir to $dest_dir."
echo ""

# 2. START IMPORTING FILES
echo "Starting importer!"
docker run --rm --name importer -v /home/nepremicnine-sledilnik/database/importer/import-data:/usr/src/nepremicnine_sledilnik/database/importer/import-data --network=nsledilnik_backend-net --env-file /home/nepremicnine-sledilnik/.env nsledilnik/importer:1.1.1 > /home/nepremicnine-sledilnik/logs/importer/importer-job-$(date +"%y-%m-%d__%H-%M").log

echo ""
echo "Finished at $(date)"
echo ""
echo ""

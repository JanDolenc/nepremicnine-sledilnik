include ../.env

#target
start-db:
	docker run --name nsledilnik-mysql -e MYSQL_ROOT_PASSWORD=nsledilnik_db -dp 3306:3306 --mount source=nsledilnik-db-vol,target=/var/lib/mysql --network=nsledilnik-db-net mysql:8.0.33

stop-db:
	docker rm -f nsledilnik-mysql

restart-db:
	$(MAKE) stop-db
	$(MAKE) start-db

query-db:
	docker exec -it nsledilnik-mysql mysql -uroot -pnsledilnik_db

bash-db:
	docker exec -it nsledilnik-mysql bash
	
# export
mysqldump-db:
	docker exec -d nsledilnik-mysql bash mysqldump -u root -pnsledilnik_db test > test_db.sql
	
copy-backup-to-host:
	docker cp nsledilnik-mysql:backup-nsledilnik-23-05-08.sql .

#import
copy-backup-from-host:
	docker cp backup-nsledilnik-23-05-08.sql nsledilnik-mysql:/

mysql-create-db:
	docker exec -d nsledilnik-mysql mysql -u root -pnsledilnik_db -e "CREATE DATABASE IF NOT EXISTS test;"


# IMPORTER SCRIPT

# Importer testing: rename imported files back to original name - remove "-imported" from the name	
rename-imported-files:
	python3 ../scripts/file_renamer.py ./import-data/archive -imported ""

# usage: make importer-build TAG=new-tag | if target is executed without new tag the default value is used
# default value
TAG = latest

importer-build:
	docker build . -t nsledilnik/importer:$(TAG)

importer-sh:
	docker exec -it importer sh

importer-rm:
	docker rm -f importer

# Start container that does NOT automatically execute the importer script. Runs indefinitely in the background. For testing.
importer-manual:
	docker run -t -d --name importer -v $(BIND_FOLDER_HOST):$(BIND_FOLDER_CONTAINER) --network=nsledilnik-db-net --env-file $(ENV_FILE) nsledilnik/importer:manual

# Start container that automatically execute the importer script. When the job is done it exits and removes itself. Log file is also made.
importer-auto:
	docker run --rm --name importer -v $(BIND_FOLDER_HOST):$(BIND_FOLDER_CONTAINER) --network=nsledilnik-db-net --env-file $(ENV_FILE) nsledilnik/importer:auto > $(IMPORTER_LOG) 
	
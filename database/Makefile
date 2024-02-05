include ../.env

TAG = dev
#target
start-db:
	docker run --name nsledilnik-db -dp 3306:3306 --mount source=nsledilnik-db-vol,target=/var/lib/mysql --env-file ../.env --network=nsledilnik-db-net nsledilnik/database:$(TAG)

start-db-no-volume:
	docker run --name nsledilnik-db -dp 3306:3306 --network=nsledilnik-db-net --env-file ../.env nsledilnik/database:$(TAG) 

stop-db:
	docker rm -f nsledilnik-db

restart-db:
	$(MAKE) stop-db
	$(MAKE) start-db

build-db:
	docker build -t nsledilnik/database:$(TAG) .

query-db:
	docker exec -it nsledilnik-db mysql -u${DB_USER1} -p${DB_USER1_PASSWORD}

bash-db:
	docker exec -it nsledilnik-db bash
	
# export
mysqldump-db:
	docker exec -d nsledilnik-db bash mysqldump -u root -pnsledilnik_db test > test_db.sql
	
copy-backup-to-host:
	docker cp nsledilnik-db:backup-nsledilnik-23-05-08.sql .

#import
copy-backup-from-host:
	docker cp backup-nsledilnik-23-05-08.sql nsledilnik-db:/

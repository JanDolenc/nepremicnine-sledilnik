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

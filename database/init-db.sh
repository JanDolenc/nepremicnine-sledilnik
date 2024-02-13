#!/bin/bash
# init db - create database and users with privileges. Disable remote access to the root user
echo "Creating default DB and users"

mysql -u root -p${MYSQL_ROOT_PASSWORD} --execute \
"CREATE DATABASE IF NOT EXISTS ${DATABASE_NAME} COLLATE utf8mb4_bin;
USE ${DATABASE_NAME};

CREATE USER '${DB_USER1}'@'%' IDENTIFIED BY '${DB_USER1_PASSWORD}';
GRANT ALL PRIVILEGES ON *.* TO '${DB_USER1}'@'%' WITH GRANT OPTION;

CREATE USER '${DB_USER2}'@'%' IDENTIFIED BY '${DB_USER2_PASSWORD}';
GRANT CREATE, INDEX, REFERENCES, SELECT, INSERT, UPDATE, DELETE ON ${DATABASE_NAME}.* TO '${DB_USER2}'@'%' WITH GRANT OPTION;

DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('%', '127.0.0.1', '::1');

FLUSH PRIVILEGES;"

echo "Finished creating default DB and users"

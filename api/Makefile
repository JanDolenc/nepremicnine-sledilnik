# target
start-dev:
	docker run -d --name nsledilnik-api-dev -v $$(pwd)/app:/usr/src/api/app -p 80:80 --network=nsledilnik-db-net --env-file ../.env nsledilnik/api:dev

stop-dev:
	docker rm -f nsledilnik-api-dev

# usage: make api-build TAG=new-tag | if target is executed without new tag the default value is used
# default value
TAG = dev 

build-api:
	docker build . -t nsledilnik/api:$(TAG)

sh-api:
	docker exec -it nsledilnik-api-dev sh

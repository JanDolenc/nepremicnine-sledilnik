# target
start-dev-bind:
	docker run -d --name nsledilnik-api-dev -v $$(pwd)/app:/usr/src/api/app -p 80:80 --network=nsledilnik-db-net --env-file ../.env nsledilnik/api:dev

start-dev:
	docker run -d --name api-dev-new  -p 8080:80 --network=nsledilnik-db-net --env-file ../.env api:dev-new

stop-dev:
	docker rm -f nsledilnik-api-dev

# usage: make api-build TAG=new-tag | if target is executed without new tag the default value is used
# default value
TAG = dev 

build-api:
	docker build . -t nsledilnik/api:$(TAG)

build-api-w-context:
	docker build -f Dockerfile ../. -t api:dev-new

sh-api:
	docker exec -it nsledilnik-api-dev sh

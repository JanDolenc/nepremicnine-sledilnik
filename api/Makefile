# target
# usage: make api-build TAG=new-tag | if target is executed without new tag the default value is used
# default value
TAG = dev 
NAME = nsledilnik-api-dev

# bind app and db_common_pkg to enable hot reload while developing api
start-dev-bind:
	docker run -d --name nsledilnik-api-dev -p 80:80 -v $$(pwd)/app:/usr/src/nepremicnine_sledilnik/api/app -v $$(pwd)/../database/db_common_pkg:/usr/src/nepremicnine_sledilnik/database/db_common_pkg --network=nsledilnik_backend-net --env-file ../.env nsledilnik/api:$(TAG)

start-dev:
	docker run -d --name api-dev -p 8080:80 --network=nsledilnik_backend-net --env-file ../.env nsledilnik/api:$(TAG)

stop-dev:
	docker rm -f $(NAME)


# when building api specify dockerfile and context which in this case is one folder up
build-api:
	docker build -f Dockerfile ../. -t nsledilnik/api:$(TAG)

sh-api:
	docker exec -it $(NAME) sh

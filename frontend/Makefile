TAG = dev

build-frontend:
	docker build . -t nsledilnik/frontend:$(TAG)

start-frontend:
	docker run --name frontend -dp 8001:80 nsledilnik/frontend:$(TAG)

stop-frontend:
	docker rm -f frontend

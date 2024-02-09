# Importer testing: rename imported files back to original name - remove "-imported" from the name	
rename-imported-files:
	python3 ../../scripts/file_renamer.py ./import-data/archive -imported ""

# usage: make importer-build TAG=new-tag | if target is executed without new tag the default value is used
# default value
# set variable per recipe
build-importer: TAG = manual-dev
build-importer:
	docker build -f Dockerfile ./.. -t nsledilnik/importer:$(TAG)


# Start container that does NOT automatically execute the importer script. Runs indefinitely in the background. For testing.
# default value

manual-importer: TAG = manual-dev
manual-importer:
	docker run -t -d --name importer -v $$(pwd)/import-data:/usr/src/nepremicnine_sledilnik/database/importer/import-data --network=nsledilnik_backend-net --env-file ../../.env nsledilnik/importer:$(TAG)

# Start container that automatically execute the importer script. When the job is done it exits and removes itself. Log file is also made.
# default value

start-importer: TAG = dev
start-importer:
	docker run --rm --name importer -v $$(pwd)/import-data:/usr/src/nepremicnine_sledilnik/database/importer/import-data --network=nsledilnik_backend-net --env-file ../../.env nsledilnik/importer:$(TAG) > ../../logs/importer/importer-job-$$(date +"%y-%m-%d__%H-%M-%S").log

stop-importer:
	docker rm -f importer

sh-importer:
	docker exec -it importer sh

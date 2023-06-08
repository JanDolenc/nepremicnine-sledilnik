# target
scrape-test:
	scrapy crawl nepremicninespider -a regija=test -a vrsta=test -O test.json

scrape-lj-mesto-s:
	scrapy crawl nepremicninespider -a regija=ljubljana-mesto -a vrsta=stanovanje -O data-lj-mesto-s.json
	
scrape-lj-mesto-h:
	scrapy crawl nepremicninespider -a regija=ljubljana-mesto -a vrsta=hisa -O data-lj-mesto-h.json

crawler-build:
	docker build . -t nsledilnik/crawler:py3.11.3-alpine

crawler-run:
	docker run -t -d --name crawler --network=flaresolverr-test_default nsledilnik/crawler:py3.11.3-alpine

crawler-stop:
	docker rm -f crawler

crawler-terminal:
	docker exec -it crawler sh

crawler-scrape:
	docker exec -d crawler scrapy crawl nepremicninespider -a regija=podravska -a vrsta=hisa -O data-podravska-h.json  

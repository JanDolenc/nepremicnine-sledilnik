import scrapy
from nepremicninescraper.items import Oglas
from nepremicninescraper.itemsloaders import OglasLoader


class NepremicninespiderSpider(scrapy.Spider):
    name = "nepremicninespider"

    def start_requests(self):
        if self.regija == 'test' and self.vrsta == 'test':
            url = 'http://127.0.0.1:5501/test-index-new-h.html'

        else:
            url = f'https://www.nepremicnine.net/oglasi-prodaja/{self.regija}/{self.vrsta}/'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Accept-language': 'en-GB,en;q=0.9,sl-SI;q=0.8,sl;q=0.7,la;q=0.6',
            'Origin': 'https://nepremicnine.net',
            'Referer': url,
        }

        req = scrapy.Request(url, headers=headers)
        yield req

    def parse(self, response):
        oglasi_on_page = response.css('div.property-box')
        regija = response.css('div.ff_regija strong::text').get()

        # oglas_item = Oglas()

        for oglas in oglasi_on_page:
            oglas_item = OglasLoader(item=Oglas(), selector=oglas)
            oglas_item.add_css('naslov', 'div.property-details a h2 ::text')
            oglas_item.add_css(
                'referencna_st', 'div.property-details a::attr(href)')
            oglas_item.add_css('url', 'div.property-details a::attr(href)')
            oglas_item.add_css(
                'posredovanje', 'div.property-details span.font-roboto ::text')
            oglas_item.add_css('cena', 'div.property-details h6 ::text')
            oglas_item.add_css('agencija', 'div.property-btn span span ::text')
            oglas_item.add_css(
                'vrsta', 'div.property-details span.font-roboto ::text')
            oglas_item.add_css('tip', 'span.tipi ::text')
            oglas_item.add_css(
                'nadstropje', 'div.property-details ul li:nth-of-type(3) ::text')
            oglas_item.add_css(
                'velikost', 'div.property-details ul li:nth-of-type(1) ::text')
            oglas_item.add_css(
                'leto_izgradnje', 'div.property-details ul li:nth-of-type(2) ::text')
            oglas_item.add_css(
                'zemljisce', 'div.property-details ul li:nth-of-type(4) ::text')
            oglas_item.add_value('regija', regija)

            yield oglas_item.load_item()

        next_page = response.css('a.next ::attr(href)').get()

        if next_page is not None:
            next_page_url = 'https://www.nepremicnine.net' + next_page
            # yield response.follow(next_page_url, callback=self.parse)

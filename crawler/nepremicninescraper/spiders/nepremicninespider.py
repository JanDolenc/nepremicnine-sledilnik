import scrapy
from scrapy.http import HtmlResponse
from nepremicninescraper.items import Oglas
from nepremicninescraper.itemsloaders import OglasLoader

import json


headers = {"Content-Type": "application/json"}

localhost = "http://localhost:8191/v1"


class NepremicninespiderSpider(scrapy.Spider):
    name = "nepremicninespider"

    def start_requests(self):
        if self.regija == 'test' and self.vrsta == 'test':
            url = 'http://127.0.0.1:5501/test-index-new-h.html'
            # oglasi z največ m2 padajoče
            # url = 'https://www.nepremicnine.net/oglasi-prodaja/hisa/?s=14'

        else:
            url = f'https://www.nepremicnine.net/oglasi-prodaja/{self.regija}/{self.vrsta}/'

        body = {
            'cmd': 'request.get',
            'session': 'scrapy-sess',
            'url': url,
            'maxTimeout': 60000
        }

        req = scrapy.Request(localhost, method='POST',
                             body=json.dumps(body), headers=headers)
        yield req

    def parse(self, response):
        response_in_json = response.json()
        if 'solution' in response_in_json:
            html_string = response_in_json['solution']['response']

            html = HtmlResponse(url='', body=html_string, encoding='utf-8')
            oglasi_on_page = html.css('div.property-box')
            regija = html.css('div.ff_regija strong::text').get()
            next_page = html.css('a.next ::attr(href)').get()

            # oglas_item = Oglas()
            for oglas in oglasi_on_page:
                oglas_item = OglasLoader(item=Oglas(), selector=oglas)
                oglas_item.add_css(
                    'naslov', 'div.property-details a h2 ::text')
                oglas_item.add_css(
                    'referencna_st', 'div.property-details a::attr(href)')
                oglas_item.add_css('url', 'div.property-details a::attr(href)')
                oglas_item.add_css(
                    'posredovanje', 'div.property-details span.font-roboto ::text')
                oglas_item.add_css('cena', 'div.property-details h6 ::text')
                oglas_item.add_css(
                    'agencija', 'meta[itemprop="name"]::attr(content)')
                oglas_item.add_css(
                    'vrsta', 'div.property-details span.font-roboto ::text')
                oglas_item.add_css('tip', 'span.tipi ::text')
                oglas_item.add_css(
                    'nadstropje', 'div.property-details ul li:nth-of-type(3)')
                oglas_item.add_css(
                    'velikost', 'div.property-details ul li:nth-of-type(1)')
                oglas_item.add_css(
                    'leto_izgradnje', 'div.property-details ul li:nth-of-type(2)')
                oglas_item.add_css(
                    'zemljisce', 'div.property-details ul li:nth-of-type(4)')
                oglas_item.add_value('regija', regija)
                oglas_item.add_value('oglas_na_strani', next_page)

                yield oglas_item.load_item()

            if next_page is not None:
                next_page_url = 'https://www.nepremicnine.net' + next_page
                # yield response.follow(next_page_url, callback=self.parse)
                # working with flaresolverr
                yield html.follow(localhost, method='POST', body=json.dumps({'cmd': 'request.get', 'session': 'scrapy-sess', 'url': next_page_url, 'maxTimeout': 60000}), headers=headers,  callback=self.parse)
            else:
                yield scrapy.Request(localhost, method='POST',
                                     body=json.dumps({'cmd': 'sessions.destroy', 'session': 'scrapy-sess'}), headers=headers)

                print('SESSION DESTROY WAS EXECUTED ----_-------->->')

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Oglas(scrapy.Item):
    naslov = scrapy.Field()
    referencna_st = scrapy.Field()
    url = scrapy.Field()
    posredovanje = scrapy.Field()
    cena = scrapy.Field()
    agencija = scrapy.Field()
    vrsta = scrapy.Field()
    tip = scrapy.Field()
    nadstropje = scrapy.Field()
    velikost = scrapy.Field()
    leto_izgradnje = scrapy.Field()
    zemljisce = scrapy.Field()
    regija = scrapy.Field()
    oglas_na_strani = scrapy.Field()

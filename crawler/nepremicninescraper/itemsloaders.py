from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class OglasLoader(ItemLoader):
    default_output_processor = TakeFirst()
    naslov_in = MapCompose(lambda x: x.strip())
    referencna_st_in = MapCompose(lambda x: x.split("o")[-1])
    # url_in = MapCompose(lambda x: 'https://www.nepremicnine.net' + x)
    posredovanje_in = MapCompose(lambda x: x.split(":")[0])
    cena_in = MapCompose(lambda x: x.split(
        "€")[0].replace('.', '').replace(',', '.').strip())
    agencija_in = MapCompose(lambda x: x.strip())
    velikost_in = MapCompose(lambda x: x.replace(' m', '').replace(',', '.'))
    zemljisce_in = MapCompose(lambda x: x.replace(' m', '').replace(',', '.'))

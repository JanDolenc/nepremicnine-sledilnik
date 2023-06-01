from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class OglasLoader(ItemLoader):
    default_output_processor = TakeFirst()
    naslov_in = MapCompose(lambda x: x.strip())
    referencna_st_in = MapCompose(lambda x: x.split("_")[-1].split("/")[0])
    posredovanje_in = MapCompose(lambda x: x.strip().split(":")[0])
    vrsta_in = MapCompose(lambda x: x.split(":")[-1].split(",")[0].strip())
    cena_in = MapCompose(lambda x: x.split(
        "€")[0].replace('.', '').replace(',', '.').strip())
    agencija_in = MapCompose(lambda x: x.strip())
    oglas_na_strani_in = MapCompose(lambda x: x.split('/')[-2])

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StringToNumberPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if (adapter.get('referencna_st')):
            adapter['referencna_st'] = int(adapter['referencna_st'])

        if (adapter.get('cena')):
            adapter['cena'] = float(adapter['cena'])

        if (adapter.get('velikost')):
            adapter['velikost'] = float(adapter['velikost'])

        if (adapter.get('leto_izgradnje')):
            adapter['leto_izgradnje'] = int(adapter['leto_izgradnje'])

        return item

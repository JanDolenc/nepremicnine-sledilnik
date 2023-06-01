# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http import HtmlResponse

from typing import Optional
from typing_extensions import TypedDict


class ValidatedData(TypedDict):
    velikost: Optional[str]
    leto_izgradnje: Optional[str]
    nadstropje: Optional[str]
    zemljisce: Optional[str]


class ValidateUlDataPipeline:
    def process_item(self, item, spider):
        validated_data: ValidatedData = {}

        # za naštete key-e izvedem kodo za čiščenje, če polje v dict item ni prazen oz obstaja
        for key in item:
            if key in ['velikost', 'leto_izgradnje', 'nadstropje', 'zemljisce']:
                value = item[key]

                # v naštete key-e trenutno shranim cel element v obliki str: <li><img src="https://www.nepremicnine.net/images/leto.svg" class="img-fluid" alt="">1971</li>
                # zato pretvorim v htmlresponse da lahko uporabim metode za pridobitev podatkov vn na enostaven način
                # na podlagi imena slike: npr leto.svg, ugotovim za katero polje gre
                if value:
                    if 'velikost' in value:
                        html = HtmlResponse(
                            url='', body=value, encoding='utf-8')

                        data = html.css(
                            'li::text').get()

                        # odstranim še enoto in zamenjam , s . kjer je to potrebno
                        validated_data['velikost'] = self.remove_unit_and_change_dec_separator(
                            data)

                    if 'leto' in value:
                        html = HtmlResponse(
                            url='', body=value, encoding='utf-8')

                        validated_data['leto_izgradnje'] = html.css(
                            'li::text').get()

                    if 'nadstropje' in value:
                        html = HtmlResponse(
                            url='', body=value, encoding='utf-8')

                        validated_data['nadstropje'] = html.css(
                            'li::text').get()

                    if 'zemljisce' in value:
                        html = HtmlResponse(
                            url='', body=value, encoding='utf-8')

                        data = html.css(
                            'li::text').get()

                        validated_data['zemljisce'] = self.remove_unit_and_change_dec_separator(
                            data)

        # save validated and cleaned data
        item['velikost'] = validated_data.get('velikost')
        item['leto_izgradnje'] = validated_data.get('leto_izgradnje')
        item['nadstropje'] = validated_data.get('nadstropje')
        item['zemljisce'] = validated_data.get('zemljisce')

        return item

    def remove_unit_and_change_dec_separator(self, data: str) -> str:
        cleaned_data = data.replace(' m', '').replace(
            '.', '').replace(',', '.')

        return cleaned_data


class AdOnPagePipeline:
    last_page: Optional[int] = None

    def process_item(self, item, spider):
        if 'oglas_na_strani' in item:
            value: str = item['oglas_na_strani']
            if value:
                self.last_page = current_page = int(value)
                # we receive the next page number so we subtract
                current_page -= 1
        else:
            # the last item doesn't have field oglas_na_strani. Next page link can't be selected because there isn't one so this field is empty at the items on the last page.
            if self.last_page:
                current_page = self.last_page

        item['oglas_na_strani'] = current_page
        return item


class StringToNumberPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if (adapter.get('referencna_st')):
            adapter['referencna_st'] = int(adapter['referencna_st'])

        if (adapter.get('cena')):
            adapter['cena'] = float(adapter['cena'])

        if (adapter.get('velikost')):
            adapter['velikost'] = float(adapter['velikost'])

        if (adapter.get('zemljisce')):
            adapter['zemljisce'] = float(adapter['zemljisce'])

        if (adapter.get('leto_izgradnje')):
            adapter['leto_izgradnje'] = int(adapter['leto_izgradnje'])

        return item

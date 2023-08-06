import os
import re
import pytz
from datetime import datetime
import fnmatch
import json
import decimal
from sqlmodel import Session, select
import sqlalchemy.orm.state

from models import Oglas, OglasCena
from database import create_db_and_tables, engine

print('---------------')
print('IMPORTER v0.0.1')
start_time = datetime.now()
print('Started at:', start_time)
print('---------------')
print()

print('LOOKING FOR FILES TO IMPORT')
print('---------------')
print('Found these files:')

files_count: int = 0
files_for_import: list[str] = []
folder_path: str = '../crawler/scraped-data-host/start/'
for filename in os.listdir(folder_path):
    if fnmatch.fnmatch(filename, 'data-*.json') and not fnmatch.fnmatch(filename, '*imported*'):
        print(filename)
        files_count += 1
        files_for_import.append(filename)


print(files_count, 'files total')
print()
print(files_for_import)
print()

print('CONNECTING & PREPARING DB')
print('---------------')
print()
create_db_and_tables()

print('STARTING TO IMPORT')
print('---------------')

current_file = files_for_import.pop(0)
print('importing file:', current_file)

with open(folder_path + current_file, 'r') as current_json_file:
    data_json = json.load(current_json_file)

    # get the date (string "YY-MM-DD") out of the current file name using regex
    match = re.search(r'\d{2}-\d{2}-\d{2}', current_file)

    # get utc timezone (int) out of string "YY-MM-DD"
    file_ts = int(pytz.utc.localize(datetime.strptime(
        match.group(), '%y-%m-%d')).timestamp())

    with Session(engine) as session:

        for ad_json in data_json:

            # check if the ad with ref_st already exists
            ad = session.exec(select(Oglas).where(
                Oglas.referencna_st == ad_json.get('referencna_st'))).first()

            """ print()
            print('THIS IS ad', ad)
            print() """

            # if ad with this ref_st does NOT exists
            if ad is None:

                # OGLAS - w this ref_st does NOT exists - insert it
                ad: Oglas = Oglas(
                    referencna_st=ad_json.get('referencna_st'), naslov=ad_json.get('naslov'), url=ad_json.get('url'), posredovanje=ad_json.get('posredovanje'), agencija=ad_json.get('agencija'), vrsta=ad_json.get('vrsta'), tip=ad_json.get('tip'), nadstropje=ad_json.get('nadstopje'), velikost=ad_json.get('velikost'), leto_izgradnje=ad_json.get('leto_izgradnje'), zemljisce=ad_json.get('zemljisce'), regija=ad_json.get('regija'))
                print('THIS is AD before commit', ad)
                session.add(ad)
                session.commit()

                # OGLAS_CENA - insert oglas_cena

                ad_price: OglasCena = OglasCena(
                    oglas_id=ad.id, ts=file_ts, cena=ad_json.get('cena'))
                session.add(ad_price)
                session.commit()
                print('this is ad PRICEE', ad_price)
                print()

            # if ad with ref_st does exists
            if ad is not None:

                # UPDATE oglas data if necessary
                print('ADD BEFORE LOOP', ad.zemljisce)
                for key, item in ad:
                    if key != 'id' and not isinstance(item, sqlalchemy.orm.state.InstanceState):

                        # convert floats to decimal
                        if isinstance(ad_json.get(key), float):
                            ad_json[key] = decimal.Decimal(
                                str(ad_json.get(key))).quantize(decimal.Decimal('.01'))

                        if item != ad_json.get(key):

                            print('values ARE NOT the same', item, type(item),
                                  'ad-json', ad_json.get(key), type(ad_json.get(key)))

                            setattr(ad, key, ad_json.get(key))

                session.add(ad)
                session.commit()

                print()
                print('AD AFTER', ad.zemljisce)
                print()

                # OGLAS_CENA - update ad price (oglas_cena) if necessary
                # ad_price = session.exec(select(OglasCena).where(
                #    OglasCena.oglas_id == ad.id).order_by(OglasCena.ts.desc()).limit(1)).all()

                ad_price = session.exec(select(OglasCena).where(
                    OglasCena.oglas_id == ad.id).order_by(OglasCena.ts.desc())).first()

                print()
                print()
                print()
                print('this is the item LATEST PRICE', ad_price,
                      datetime.fromtimestamp(ad_price.ts))
                print()
                print()
                print()

                result = file_ts - ad_price.ts
                print('resULT', result)

                ad_json['cena'] = decimal.Decimal(
                    str(ad_json.get('cena'))).quantize(decimal.Decimal('.01'))

                # update price if it's changed or older than 5 days = 432000 seconds - every other job
                if ad_price.cena != ad_json.get('cena') or file_ts - ad_price.ts > 432000:
                    print('the PRICE IS NOT the same')
                    ad_price = OglasCena(
                        oglas_id=ad.id, ts=file_ts, cena=ad_json.get('cena'))

                    session.add(ad_price)
                    session.commit()

                print()
                print('the new PRICE IS', ad_price,
                      datetime.fromtimestamp(ad_price.ts), 'type', type(ad_price.cena))

            # model for lokacija
            # location = Lokacija(naziv=ad['regija'])

        # print()
        # print(data_json)

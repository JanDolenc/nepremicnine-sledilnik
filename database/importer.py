import os
from datetime import datetime
import fnmatch
import json
from sqlmodel import Session, select

from models import Nepremicnina, Oglas, Lokacija, Agencija
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

    with Session(engine) as session:

        for ad_json in data_json:
            # print('this is data_item', ad)
            # print()

            # check if the ad with ref_st already exists
            ad_w_ref_exists = session.exec(select(Oglas).where(
                Oglas.referencna_st == ad_json.get('referencna_st'))).first()

            """ print()
            print('THIS IS ad', ad_w_ref_exists)
            print() """

            # if ad with this ref_st does NOT exists
            if ad_w_ref_exists is None:

                # AGENCY - check if it exists
                agency = session.exec(select(Agencija).where(
                    Agencija.naziv == ad_json.get('agencija'))
                ).first()

                # agency does NOT exists insert it
                if agency is None:
                    agency = Agencija(naziv=ad_json.get('agencija'))
                    # session.add(agency)
                    # session.commit()

                # LOCATION - check if it exists
                location = session.exec(select(Lokacija).where(
                    Lokacija.regija == ad_json.get('regija'))
                ).first()

                # location does NOT exists insert it
                if location is None:
                    location = Lokacija(regija=ad_json.get('regija'))
                    session.add(location)
                    session.commit()

                    # session.refresh(location)

                # NEPREMICNINA - check if it exists
                property = session.exec(select(Nepremicnina).where(
                    Nepremicnina.vrsta == ad_json.get('vrsta'),
                    Nepremicnina.tip == ad_json.get('tip'),
                    Nepremicnina.nadstropje == ad_json.get('nadstropje'),
                    Nepremicnina.velikost == ad_json.get('velikost'),
                    Nepremicnina.leto_izgradnje == ad_json.get('leto_izgradnje'),
                    Nepremicnina.zemljisce == ad_json.get('zemljisce'),
                    Nepremicnina.lokacija == Lokacija(
                        id=location.id, regija=location.regija),
                )
                ).first()

                print()
                print('VALUE OF property BEFORE iff', property)

                # if property with exactly the same params does NOT exist - insert it
                if property is None:
                    property = Nepremicnina(vrsta=ad_json.get('vrsta'), tip=ad_json.get('tip'), nadstropje=ad_json.get('nadstropje'), velikost=ad_json.get(
                        'velikost'), leto_izgradnje=ad_json.get('leto_izgradnje'), zemljisce=ad_json.get('zemljisce'), lokacija_id=location.id)
                    session.add(property)
                    session.commit()

                    #session.refresh(location)
                    #session.refresh(property)
                    print('INSERT it AND REFRESH IITT')

                print()
                print('this LocaTION', location)
                print()
                print('THIS IS AGENcy', agency)
                print()
                print('THIS IS PrOPertY', property)
                print()
                print()

                # OGLAS - w this ref_st does NOT exists - insert it
                ad: Oglas = Oglas(
                    referencna_st=ad_json.get('referencna_st'), naslov=ad_json.get('naslov'), url=ad_json.get('url'), posredovanje=ad_json.get('posredovanje'), nepremicnina_id=property.id, agencija_id=agency.id)
                print('THIS is AD before commit', ad)
                session.add(ad)
                session.commit()

                print('THIS is AD AFTERR commit', ad)


                # insert oglas_cena

            # if ad with ref_st does exists
            if ad_w_ref_exists is not None:

                print()
                print('AD W ref EXISTS', ad_w_ref_exists)
                print()
                print()

            # model for lokacija
            # location = Lokacija(naziv=ad['regija'])

        # print()
        # print(data_json)

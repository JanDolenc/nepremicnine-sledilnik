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

        for ad in data_json:
            # print('this is data_item', ad)
            # print()

            # check if the ad with ref_st already exists
            ad_w_ref_exists = session.exec(select(Oglas).where(
                Oglas.referencna_st == ad.get('referencna_st'))).first()

            """ print()
            print('THIS IS ad', ad_w_ref_exists)
            print() """

            # if ad with this ref_st does NOT exists
            if ad_w_ref_exists is None:

                # AGENCY - check if it exists
                agency = session.exec(select(Agencija).where(
                    Agencija.naziv == ad.get('agencija'))
                ).first()

                # agency does NOT exists insert it
                if agency is None:
                    agency = Agencija(naziv=ad.get('agencija'))
                    # session.add(agency)
                    # session.commit()

                # LOCATION - check if it exists
                location = session.exec(select(Lokacija).where(
                    Lokacija.regija == ad.get('regija'))
                ).first()

                # location does NOT exists insert it
                if location is None:
                    location = Lokacija(regija=ad.get('regija'))
                    # session.add(location)
                    # session.commit()

                    # session.refresh(location)

                # insert nepremicnino

                # insert oglas

                # insert oglas_cena

            # if ad with ref_st does exists
            if ad_w_ref_exists is not None:

                print()

            # model for lokacija
            # location = Lokacija(naziv=ad['regija'])

        # print()
        # print(data_json)

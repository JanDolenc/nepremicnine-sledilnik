import os
import sys
import re
import pytz
import shutil
from time import sleep
from datetime import datetime
import fnmatch
import json
import decimal
from sqlmodel import Session, select, func
import sqlalchemy.orm.state

from models import Oglas, OglasCena, regija_mapped, vrsta_mapped
from database import create_db_and_tables, engine


def print_job_stats_when_error():
    if job_stats:
        print(
            f"\nImporter exited but still successfully imported ({job_stats[-1].get('file_number')}) files in this order")
        print(json.dumps(job_stats, indent=4))
    else:
        print(f"\n\nIMPORTER may (partialy) import one file ({current_file}).")


print('---------------')
print('IMPORTER v0.0.1')
start_time = datetime.now()
print('Started at:', start_time)
print('---------------')
print()

print('LOOKING FOR FILES TO IMPORT')
print('---------------')

files_count: int = 0
files_for_import: list[str] = []
job_stats: list[dict] = []
folder_path: str = '../crawler/scraped-data-host/start/'

for filename in os.listdir(folder_path):

    file_size = os.stat(folder_path + filename).st_size

    # import only files with appropriate name and are not empty
    if fnmatch.fnmatch(filename, 'data-*.json') and not fnmatch.fnmatch(filename, '*imported*') and file_size > 0:

        # get the date (string "YY-MM-DD") out of the current file name using regex
        match = re.search(r'\d{2}-\d{2}-\d{2}', filename)

        if match:
            files_for_import.append((filename, match.group(0)))
            files_count += 1

files_for_import = sorted(files_for_import, key=lambda x: x[1])


print('Found these files:')
for filename, file_date in files_for_import:
    print(filename, file_date)

print(files_count, 'files total')
print()

if not files_for_import:
    sys.exit('No files to import. Job is finished!')

print('CONNECTING & PREPARING DB')
print('---------------')
print()
create_db_and_tables()

print('STARTING TO IMPORT')
print('---------------')

for index, (current_file, file_date) in enumerate(files_for_import):
    print()
    print()
    print()
    print('importing file:', current_file)

    current_import_start_ts: int = int(datetime.now().timestamp())
    print('current import start time: ',
          datetime.fromtimestamp(current_import_start_ts))

    with open(folder_path + current_file, 'r') as current_json_file:
        data_json = json.load(current_json_file)

        # get utc timezone (int) out of string "YY-MM-DD"
        file_ts = int(pytz.utc.localize(
            datetime.strptime(file_date, '%y-%m-%d')).timestamp())

        # get regija label from file name data-REGIJA-x-yy-mm-dd | find a match and take out first string
        regija_label = re.search(
            r'gorenjska|lj-mesto|j-primorska|podravska|lj-okolica', current_file).group(0)
        file_regija = regija_mapped.get(regija_label)

        # get vrsta label from file name data-regija-X-yy-mm-dd | find a match, take out first string "-s-"" or "-h-" then take second character from the string
        vrsta_label = re.search(r'-s-|-h-', current_file).group(0)[1]
        file_vrsta = vrsta_mapped.get(vrsta_label)

        print()
        print('regija in filename', regija_label, file_regija)
        print('VRSTA in filename', vrsta_label, file_vrsta)
        print()

        # count how many times the loop for items in json file executes
        items_loop_execution_count: int = 0

        ads_up_to_date_count: int = 0

        with Session(engine) as session:

            # get latest record for current regija and vrsta
            db_latest_record = session.exec(select(Oglas.id, Oglas.regija, Oglas.vrsta, Oglas.updated_ts).where(
                (Oglas.regija == file_regija) & (Oglas.vrsta == file_vrsta)).order_by(Oglas.updated_ts.desc())).first()

            print('latest ReCoRD in db -------',
                  db_latest_record, datetime.fromtimestamp(db_latest_record.updated_ts)) if db_latest_record is not None else print('latest ReCoRD in db -----', db_latest_record)

            # if current file data is not newer or equal that db_latest_record display warning
            if db_latest_record is not None and not (db_latest_record.updated_ts <= file_ts):
                print_job_stats_when_error()
                sys.exit(f"IMPORTER EXITED, WARNING!\nLooks like the file {current_file} is not the latest - meaining the latest records in db have newer date than those in json file. If we would continue the data (price etc.) would be updated with values that are not the latest - data would be spoiled for current regija-vrsta. \n\nLatest db record: {db_latest_record.id, db_latest_record.regija, db_latest_record.vrsta}, {datetime.fromtimestamp(db_latest_record.updated_ts)} \nCurrent file: {file_regija, file_vrsta} {datetime.fromtimestamp(file_ts)} <- problem")

            for ad_json in data_json:

                # check if the ad with ref_st already exists
                ad_db = session.exec(select(Oglas).where(
                    Oglas.referencna_st == ad_json.get('referencna_st'))).first()

                print()
                print('This is loop run number ',
                      items_loop_execution_count, ' ----------------------')
                print('Does AD exists?', ad_db)

                # if ad with this ref_st does NOT exists
                if ad_db is None:

                    # OGLAS - w this ref_st does NOT exists - insert it
                    oglas_created_at: int = int(datetime.now().timestamp())

                    ad: Oglas = Oglas(
                        referencna_st=ad_json.get('referencna_st'), naslov=ad_json.get('naslov'), url=ad_json.get('url'), posredovanje=ad_json.get('posredovanje'), agencija=ad_json.get('agencija'), vrsta=ad_json.get('vrsta'), tip=ad_json.get('tip'), nadstropje=ad_json.get('nadstropje'), velikost=ad_json.get('velikost'), leto_izgradnje=ad_json.get('leto_izgradnje'), zemljisce=ad_json.get('zemljisce'), regija=ad_json.get('regija'), detected_ts=file_ts, updated_ts=file_ts, created_at=oglas_created_at, updated_at=oglas_created_at)

                    print('AD does NOT exists. This will be inserted', ad)
                    session.add(ad)
                    session.commit()

                    # OGLAS_CENA - insert oglas_cena
                    ad_price: OglasCena = OglasCena(
                        oglas_id=ad.id, record_ts=file_ts, cena=ad_json.get('cena'), created_at=int(datetime.now().timestamp()))

                    print(
                        'this is ad PRICEE that doesnt exits yet -> will be inserted', ad_price)
                    session.add(ad_price)
                    session.commit()
                    print()

                # if ad with ref_st DOES exists
                if ad_db is not None:

                    # UPDATE oglas data if necessary
                    # check value of every item of ad stored in db
                    for key, item in ad_db:

                        if key != 'id' and key != 'detected_ts' and key != 'updated_ts' and key != 'created_at' and key != 'updated_at' and not isinstance(item, sqlalchemy.orm.state.InstanceState):

                            # convert floats to decimal
                            if isinstance(ad_json.get(key), float):
                                ad_json[key] = decimal.Decimal(
                                    str(ad_json.get(key))).quantize(decimal.Decimal('.01'))

                            # store new value if the db value is out of date
                            if item != ad_json.get(key):

                                print('values ARE NOT the same', item, type(item),
                                      'ad-json', ad_json.get(key), type(ad_json.get(key)))

                                setattr(ad_db, key, ad_json.get(key))

                    if session.is_modified(ad_db):

                        setattr(ad_db, 'updated_ts', file_ts)

                        setattr(ad_db, 'updated_at', int(
                                datetime.now().timestamp()))

                        print('Ad does exits and it was updated', ad_db)
                        session.add(ad_db)
                        session.commit()
                        print()
                        print('THe commit JUST RANN')
                    else:
                        print()
                        print('AD exists but was not updated')

                        ads_up_to_date_count += 1

                    print()
                    print()
                    print()

                    # OGLAS_CENA - update (oglas_cena) if necessary
                    ad_price = session.exec(select(OglasCena).where(
                        OglasCena.oglas_id == ad_db.id).order_by(OglasCena.record_ts.desc())).first()

                    print()
                    print()
                    print()
                    print('this is the item LATEST PRICE in db', ad_price,
                          datetime.fromtimestamp(ad_price.record_ts))
                    print()
                    print()
                    print()

                    result = file_ts - ad_price.record_ts
                    print('resULT', result)

                    ad_json['cena'] = decimal.Decimal(
                        str(ad_json.get('cena'))).quantize(decimal.Decimal('.01'))

                    # update price (insert new record) if it's changed or older than 5 days = 432000 seconds - every other job
                    if ad_price.cena != ad_json.get('cena') or file_ts - ad_price.record_ts > 432000:
                        print('the PRICE IS NOT the same')
                        ad_price = OglasCena(
                            oglas_id=ad_db.id, record_ts=file_ts, cena=ad_json.get('cena'), created_at=int(datetime.now().timestamp()))

                        session.add(ad_price)
                        session.commit()

                        print()
                        print('the new PRICE IS', ad_price,
                              datetime.fromtimestamp(ad_price.record_ts), 'type', type(ad_price.cena))
                    else:
                        print('THe price was not updateD')

                items_loop_execution_count += 1

            # how many inserts - new rows and updates happend in the current import
            current_import_changes_count = session.exec(select(func.count()).where(
                Oglas.updated_at >= current_import_start_ts)).first()

    ads_in_file_count: int = len(data_json)

    # move current file to archive folder and rename it to *-imported.json if import was successful
    archive_folder_path = '../crawler/scraped-data-host/start/archive/'

    if ads_in_file_count != current_import_changes_count + ads_up_to_date_count:
        print_job_stats_when_error()
        sys.exit('ERROR, IMPORTER EXITED! Something went wrong when inserting / updating ' + str(current_file) +
                 '. Please manually check how many items (ads) were (not) inserted. The loop that inserts items have ran ' + str(items_loop_execution_count) + ' times before failing. If possible try reverting db and try again.')
    else:
        job_stats.append(
            {
                'file_number': index + 1,
                'file_name': current_file,
                'import_start_time': str(datetime.fromtimestamp(current_import_start_ts)),
                'changes_made': current_import_changes_count,  # new records or updates
                'ads_not_changed': ads_up_to_date_count,  # already up to date
                'number_of_ads_in_file': ads_in_file_count
            }
        )

        print()
        print(f'File import success! {current_file}')
        print('Renaming file and moving it to archive...')

        shutil.move(folder_path + current_file, archive_folder_path +
                    current_file[:-5] + '-imported.json')

    # sleep for a second to prevent ads in the next file to have the same updated_at value, which is used to determine if the current file import was successful
    last_file_to_import = True if index == len(files_for_import) - 1 else False
    if not last_file_to_import:
        sleep(1)

print()
print()

end_time = datetime.now()


# currently stats don't represent the whole picture. Changes in table oglas_cena are not included
print('IMPORTER JOB STATS | informative based only on oglas table!!')
print('------------------------------------------------------------')
print(f'Start time: {start_time}')
print(f'End time:   {end_time}')
print(
    f"Successfully imported ({job_stats[-1].get('file_number')}) files in this order")
print(json.dumps(job_stats, indent=4))
print()

total_changes_made: int = 0
total_ads_not_changed: int = 0
total_ads_in_files: int = 0

for item in job_stats:
    total_changes_made += item.get('changes_made')
    total_ads_not_changed += item.get('ads_not_changed')
    total_ads_in_files += item.get('number_of_ads_in_file')

print(f'Total changes made / new records or updates: {total_changes_made}')
print(f'Total ads not changed / already up to date: {total_ads_not_changed}')
print(f'Total number of ads in files (not unique): {total_ads_in_files}')
print()
print('Success! Importer finished! Job is done!')

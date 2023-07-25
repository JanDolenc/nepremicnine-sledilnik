# TODO look for files that needs to be imported to db
# look for files that dont have word imported in it and it is in json format
import os
from datetime import datetime
import fnmatch
import json

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

print('STARTING TO IMPORT')
print('---------------')

current_file = files_for_import.pop(0)
print('importing file:', current_file)

with open(folder_path + current_file, 'r') as f:
    data = json.load(f)

print(data)

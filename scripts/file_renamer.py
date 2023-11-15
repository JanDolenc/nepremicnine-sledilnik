import os
import sys

# usage
# python3 file_renamer.py path/to/folder/w/files text-to-remove new-text


folder_path: str = sys.argv[1]
remove_txt: str = sys.argv[2]
new_txt: str = sys.argv[3]

for filename in os.listdir(folder_path):
    if remove_txt in filename:
        new_filename = filename.replace(remove_txt, new_txt)
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

print("FINISHED")

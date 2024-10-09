import os
import shutil


download_dir = 'project26/Downloads'

for root, dirs, files in os.walk(download_dir):
    # for file in files:
    #     filepath = os.path.join(root, file)
    #     print(filepath)
    #     os.remove(filepath)

    for dir in dirs:
        dirpath = os.path.join(root, dir)
        print(dirpath)
        shutil.rmtree(dirpath)

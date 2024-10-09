import os
import shutil


download_dir = 'project26/Downloads'

for root, dirs, files in os.walk(download_dir):
    for file in files:
        filepath = os.path.join(root, file)
        print(filepath)
        os.remove(filepath)

    for dir in dirs:
        dirpath = os.path.join(root, dir)
        print(dirpath)
        shutil.rmtree(dirpath)

# NOTE! shutil.rmtree() removes entire directory and its content

# if you want to move file to other file
for root, dirs, files in os.walk(download_dir):
    for file in files:
        filepath = os.path.join(root, file)
        print(filepath)
        # filepath is old filepath of a file. os.path.join('bakcup', file) will be a new filepath
        shutil.move(filepath, os.path.join('backup', file))

import os
import hashlib
 
# Function to calculate SHA-256 hash of a file
def get_content(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        hash_value = hashlib.sha256(content).hexdigest()
        return hash_value
 
# Directory path containing files with potential duplicates
directory_path = "files-duplicate"
 
# Dictionary to store file hashes
hashes = {}
 
# Traverse through each file in the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        filepath = os.path.join(root, filename)
        filehash = get_content(filepath)
        if filehash in hashes:
            print(f"Removing duplicate file: {filepath}")
            os.remove(filepath)
        else:
            hashes[filehash] = filepath
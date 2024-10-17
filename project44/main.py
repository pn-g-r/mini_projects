import os
import imagehash
from PIL import Image


hashsize = 8
hashes = {}

for filename in os.listdir('project44/photos'):
    filepath = os.path.join('project44/photos', filename)

    with Image.open(filepath) as img:
        img_hash = str(imagehash.average_hash(img, hashsize)
)
        if img_hash in hashes:
            print("Duplicate found", filename)
            print("Original file", hashes[img_hash])
        else:
            hashes[img_hash] = filename
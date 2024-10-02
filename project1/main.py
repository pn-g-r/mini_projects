import os
from datetime import datetime

directory = 'files'

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)

    with open(filepath) as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

    day = datetime.now().strftime("%Y-%m-%d")

    new_filename = f'{filename[:4]}-{word_count}-{day}.txt'

    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)
import os

filepath = os.walk('project42/files')

def get_content(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        return content

file_contents = {}

for root, dirs, files in filepath:
    for filename in files:
        filepath = os.path.join(root, filename)
        content = get_content(filepath)
        if content in file_contents:
            os.remove(filepath)
        else:
            file_contents[content] = filepath
import os
import re

directory = 'documents'

filenames = os.listdir(f"project11/{directory}")

all_emails = []

for filename in filenames:
    with open(f"project11/{directory}/{filename}", 'r') as file:
        content = file.read()

    emails = re.findall(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}", content)
    all_emails.extend(emails)

print(all_emails)
import os

directory = 'project2'

filename = os.path.join(directory, "example.txt")

with open(filename) as file:
    text = file.read()


words = text.split()

reversed_words = []

for word in words:
    word = word[::-1]
    reversed_words.append(word)

print(reversed_words)

with open("project2/reversed_text.txt", 'w') as file:
    file.write(' '.join(reversed_words))
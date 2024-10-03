import glob

filepaths = glob.glob('project15/text_files/*.txt')


word_counter = {}
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()

        words = content.split()

        for word in words:
            if not word in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] += 1

print(word_counter)

with open('project15/word_frequences.txt', 'w') as file:
    for word, count in word_counter.items():
        
        file.write(f'{word}: {count}\n')
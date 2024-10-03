def remove_punctuation(text):
    punctuation = ".,!?(){}[]/"
    for char in punctuation:
        text = text.replace(char, '')
    return text

text = input("Enter a block of text for analysis\n")
characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("!") + text.count("?")
word_frequency = {}

word_list = remove_punctuation(text).lower().split()

for word in word_list:
    if not word in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

most_frequent_word = max(word_frequency, key=word_frequency.get)
print("Text Analysis Results")
print("-" * 20)
print(f"Total characters: {characters}")
print(f"Total words: {words}")
print(f"Total sentences: {sentences}")
print(f"Most Frequent word: {most_frequent_word}")
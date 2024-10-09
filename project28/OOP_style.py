class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path) as file:
            text = file.read()
        return text

    def write(self, content):
        with open(f"project28/reversed.txt", 'w') as file:
            file.write(content)

class Text:
    def __init__(self, input_text):
        self.input_text = input_text

    def reverse_words(self):
        words = self.input_text.split()
        reversed_words = []
        for word in words:
            word = word[::-1]
            reversed_words.append(word)
        reversed_text = " ".join(reversed_words)
        return reversed_text
        
file = File('project28/example.txt')
content = file.read()

text = Text(content)
reversed_text = text.reverse_words()

file.write(reversed_text)
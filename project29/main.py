import os
import matplotlib.pyplot as plt

directory = 'project29/files'

file_names = []
numbers = []

for filename in sorted(os.listdir(directory)):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path) as file:
            number = float(file.read().strip())
            numbers.append(number)
            file_names.append(filename[:-4])

plt.figure(figsize=(10, 6))
plt.plot(file_names, numbers, marker='o', linestyle='-', color='b')
plt.title("Numbers from Text Files")
plt.xlabel("File name")
plt.ylabel("Number")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
from datetime import datetime

todo_items = []

while True:
    todo = input("Enter your todo items for today. Type 'done' to save and exit ")
    if todo == 'done':
        break
    todo_items.append(todo + '\n')


day = datetime.now().strftime("%A")
filename = f"{day}.txt"
with open(f'project7/{filename}', 'w') as file:
    file.write(''.join(todo_items))
from flask import Flask
import json

app = Flask(__name__)


with open('project6/books.json') as file:
    books = json.load(file)


@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return book
    else:
        return "book not found"

@app.route('/')
def index():
    return "Homepage"


app.run(debug=True)
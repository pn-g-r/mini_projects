from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    pass


app.run(debug=True)
from flask import Flask, render_template
import requests

api_key = "59febdff2a9b443f9e54abf4fa50aa4b"

url = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&q=business"
app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return render_template('project24/index.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
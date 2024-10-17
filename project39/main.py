import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Mathematics"

content = requests.get(url).text

soup = BeautifulSoup(content, 'html.parser')

result = soup.select("li[id^='cite']")

for i in result:
    print(i.get_text())
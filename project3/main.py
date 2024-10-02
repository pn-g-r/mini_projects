import requests
import inspect

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
content = response.json()

country = "Iceland"

for c in content:
    country_name = c['name']['common']
    if country_name == country:
        capital = c['capital']

content[0]['currencies']
print(content[0]['currencies']['SHP']['name'])

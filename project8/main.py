import requests


month = 10
day = 15

url = f'https://history.muffinlabs.com/date/{month}/{day}'

response = requests.get(url)
data = response.json()
events = data['data']['Events']

for event in events:
    print(f"Year: {event['year']}")
    print(f"Description: {event['text']}")
    print(f"Link: {event['links'][0]['link']}")
    print("\n")
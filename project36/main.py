import requests

API_KEY = "455dbe1351d7fcdc647737d41cba41b5"


def get_temperature(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    return temp

city = input("Enter city: ")
temperature = get_temperature(city)

print(f"Current temperature in {city}: {temperature}")
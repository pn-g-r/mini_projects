import requests
 
# Replace with your OpenWeatherMap API key
API_KEY = "455dbe1351d7fcdc647737d41cba41b5"
 
def get_temperature(city, units='metric'):
    """Fetches the current temperature for a given city in specified units.
 
    Args:
      city: The name of the city to get weather data for.
      units: The units of temperature ('metric' for Celsius, 'imperial' for Fahrenheit).
 
    Returns:
      The current temperature.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url)
 
    data = response.json()
    temp = data["main"]["temp"]
    return temp
 
def format_temperature(temp, units):
    """Formats the temperature with the appropriate unit.
 
    Args:
      temp: The temperature value.
      units: The units of temperature ('metric' for Celsius, 'imperial' for Fahrenheit).
 
    Returns:
      A string containing the formatted temperature.
    """
    if units == 'metric':
        unit_label = "°C"
    else:
        unit_label = "°F"
    return f"{temp}{unit_label}"
 
city = input("Enter City: ").strip()
units = input("Choose temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()
units = 'metric' if units != 'F' else 'imperial'
 
temperature = get_temperature(city, units)
formatted_temp = format_temperature(temperature, units)
print(f"Current temperature in {city}: {formatted_temp}")
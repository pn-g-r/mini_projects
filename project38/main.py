import requests
from bs4 import BeautifulSoup

url = "https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071"

# Send a GET request to fetch the content of the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    content = response.text

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Try to find the element containing the temperature
    temp_element = soup.find(class_="myforecast-current-lrg")

    # Check if the temperature element was found
    if temp_element:
        temp = temp_element.get_text()
        print(f"Temperature: {temp}")
    else:
        print("Temperature element not found.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

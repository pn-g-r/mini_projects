from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver (using Chrome in this case)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the weather website
driver.get("https://www.weather.gov/ohx/")

# Let the page load fully before scraping
driver.implicitly_wait(10)  # waits up to 10 seconds for the page to load

# Try to find the element containing the temperature
try:
    temp_element = driver.find_element(By.ID, "myfcst-tempf")
    temp = temp_element.text
    print(f"Temperature: {temp}")
except:
    print("Temperature element not found.")

# Close the browser
driver.quit()

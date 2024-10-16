from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Create an instance of Chrome Options
chrome_options = Options()
chrome_options.add_argument("--start-fullscreen")  # This argument opens Chrome in full-screen

# Initialize the WebDriver with the full-screen option
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

username_field.send_keys('pythonstudent')
password_field.send_keys('PythonStudent123$')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(login_button))
login_button.click()

time.sleep(3)
driver.quit()

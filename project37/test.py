from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Function to extract prices from a page and print only relevant prices and links
def extract_prices(driver, url, price_threshold):
    driver.get(url)

    # Use WebDriverWait to wait for the price elements to load
    try:
        price_elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, "//p[@class='flex items-center undefined']"))
        )
    except Exception as e:
        print(f"Error waiting for price elements: {e}")
        return

    # Extract and print only the relevant prices (below the threshold)
    for price_element in price_elements:
        price_text = price_element.text.strip().replace(",", "")  # Clean up the price text
        try:
            price_value = int(price_text)  # Convert to integer for comparison
        except ValueError:
            continue  # Skip if the conversion fails

        # Print only prices below the threshold
        if price_value < price_threshold:
            print(f"Price found: {price_value}")
            
            # Traverse up to find the parent div
            try:
                # Find the parent div that contains the link
                parent_div = price_element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'md:pl')]")

                # Look for the link within the parent div that contains the word 'offerType'
                link = parent_div.find_element(By.XPATH, ".//a[contains(@href, 'offerType')]")

                # Print the price and link nicely formatted
                if link:
                    print(f"Price: {price_value} | Link: {link.get_attribute('href')}")
            except Exception as e:
                print(f"Error finding or printing the link: {e}")

# Base URL for pagination
base_url = 'https://www.myauto.ge/ka/s/iyideba-manqanebi-toyota-rav-4-2019-2023?vehicleType=0&bargainType=0&mansNModels=41.1128&yearFrom=2019&yearTo=2023&currId=3&mileageType=1&fuelTypes=6&locations=2.3.4.7.15.30.113.52.37.48.47.44.41.31.40.39.38.36.53.54.16.14.13.12.11.10.9.8.6.5.55.56.57.59.58.61.62.63.64.66.71.72.74.75.76.77.78.80.81.82.83.84.85.86.87.88.91.96.97.101.109.116.119.122.127.131.133&customs=1&page='

# Set a price threshold (e.g., 57,300)
price_threshold = 57300

# Loop through pages and extract prices
for page_num in range(1, 5):  # Adjust range for more pages
    page_url = base_url + str(page_num)
    extract_prices(driver, page_url, price_threshold)

# Close the browser when done
driver.quit()

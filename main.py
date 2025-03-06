from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

def open_link_and_copy_data(url, postman_data_xpath):
    # Set up the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    try:
        # Open the given URL
        driver.get(url)
        time.sleep(5)  # Wait for the page to load
        
        # Find the Postman data element
        postman_data_element = driver.find_element(By.XPATH, postman_data_xpath)
        
        # Copy the data to clipboard
        postman_data_element.send_keys(Keys.CONTROL, 'a')  # Select all text
        postman_data_element.send_keys(Keys.CONTROL, 'c')  # Copy to clipboard
        time.sleep(2)  # Give time for clipboard update
        
        # Get copied data
        copied_data = pyperclip.paste()
        print("Copied Postman Data:", copied_data)
        
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

# Example usage
postman_url = "https://your-postman-url.com"  # Replace with actual URL
postman_data_xpath = "//div[@class='postman-data']"  # Replace with actual XPath
open_link_and_copy_data(postman_url, postman_data_xpath)

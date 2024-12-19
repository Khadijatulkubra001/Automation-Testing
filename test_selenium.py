from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

# Set up ChromeDriver
driver = webdriver.Chrome()

#Buying product at an e-commmerce store
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

expected_title = "Swag Labs"
actual_title = driver.title

# Print the page title
print("Page Title:", driver.title)
assert expected_title in actual_title, f"Title mismatch! Expected '{expected_title}', but got '{actual_title}'"
print("Page title verified successfully.")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "item_4_title_link").click()
driver.find_element(By.NAME, "add-to-cart").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.NAME, "checkout").click()
driver.find_element(By.NAME, "firstName").send_keys("Khadija")
driver.find_element(By.NAME, "lastName").send_keys("Test")
driver.find_element(By.NAME, "postalCode").send_keys("12345")
time.sleep(2)
driver.find_element(By.NAME, "continue").click()
driver.find_element(By.NAME, "finish").click()
time.sleep(5)
driver.quit()

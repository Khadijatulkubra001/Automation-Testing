from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import time

@pytest.fixture(scope="class")
def setup_class(request):
    # Setup ChromeDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

class TestSwagLabs:

    def test_standard_user(self, setup_class):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        expected_title = "Swag Labs"
        actual_title = driver.title
        assert expected_title in actual_title, f"Title mismatch! Expected '{expected_title}', but got '{actual_title}'"
        print("Page title verified successfully.")
        
        # Standard user login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Buying product
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
        
        # Logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        element = driver.find_element(By.ID, "logout_sidebar_link")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def test_problem_user(self, setup_class):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Login as a different user (problem user)
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element((By.CLASS_NAME, "shopping_cart_badge"))
            )
            print("Cart badge disappeared, cart is empty.")
        except TimeoutException:
            cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            assert cart_count == "0", f"Expected cart count to be 0 but got '{cart_count}'"

        driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()

        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.NAME, "firstName").send_keys("Khadija")
        driver.find_element(By.NAME, "lastName").send_keys("Test")
        driver.find_element(By.NAME, "postalCode").send_keys("12345")
        time.sleep(2)
        driver.find_element(By.NAME, "continue").click()
        try:
            finish_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "finish"))
            )
            print("Navigation successful: 'Finish' button found.")
        except TimeoutException:
            print("Failed to navigate: 'Finish' button not found.")
            assert False, "Navigation to new page failed."

        finish_button.click()
        time.sleep(5)

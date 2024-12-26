from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import time
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="class")
def setup_class(request):
    #Setup Chrome
    driver = webdriver.Chrome()
    driver.get("http://automationexercise.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

class TestAutomationWebsite():

    #Test Case 1: Register User
    def test_RegisterUser(self, setup_class):
        driver = self.driver
        assert "Automation" in driver.title, f"Something is wrong."
        driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
        EC.presence_of_element_located((By.NAME, 'New User Signup!'))
        driver.find_element(By.NAME, 'name').send_keys("User123")
        driver.find_element(By.CSS_SELECTOR, '[data-qa = "signup-email"]').send_keys("user_test16@gmail.com")
        driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-button"]').click()
        EC.presence_of_element_located((By.CLASS_NAME, 'title text-center'))
        driver.find_element(By.ID, "id_gender2").click()
        driver.find_element(By.ID, 'password').send_keys("123Abc!")
        # Wait for the dropdown to be clickable
        days_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'days'))
        )
        select = Select(days_dropdown)
        select.select_by_index(5)
        dropdown = driver.find_element(By.ID, 'months')
        select = Select(dropdown)
        select.select_by_index(5)
        dropdown = driver.find_element(By.ID, 'years')
        select = Select(dropdown)
        select.select_by_index(5)
        driver.find_element(By.ID, 'first_name').send_keys("dadds")
        driver.find_element(By.ID, 'last_name').send_keys("daddsdsad")
        driver.find_element(By.ID, 'address1').send_keys("Address 234")
        dropdown = driver.find_element(By.ID, 'country')
        select = Select(dropdown)
        select.select_by_visible_text('Canada')
        driver.find_element(By.ID, 'state').send_keys("State 1")
        driver.find_element(By.ID, 'city').send_keys("Toronto")
        driver.find_element(By.ID, 'zipcode').send_keys("55555")
        driver.find_element(By.ID, 'mobile_number').send_keys("123456789")
        button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="create-account"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        EC.presence_of_element_located((By.CLASS_NAME, 'title text-center'))
        driver.find_element(By.CSS_SELECTOR, '[data-qa="continue-button"]').click()
        EC.presence_of_element_located((By.CLASS_NAME, 'fa fa-user'))
        logout_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/logout']"))
        )
        logout_link.click()
       

    def test_CorrectLogin(self, setup_class):
        driver = self.driver
        #driver.get("http://automationexercise.com/")
        driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
        EC.presence_of_element_located((By.NAME, 'Login to your account'))
        driver.find_element(By.CSS_SELECTOR, '[data-qa="login-email"]').send_keys("user_test16@gmail.com")
        driver.find_element(By.CSS_SELECTOR, '[data-qa="login-password"]').send_keys("123Abc!")
        driver.find_element(By.CSS_SELECTOR, '[data-qa="login-button"]').click()
        EC.presence_of_element_located((By.NAME, 'Logged in as User123'))
        delete_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/delete_account']"))
        )
        delete_link.click()
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="account-deleted"]'))
        driver.find_element(By.CSS_SELECTOR, '[data-qa="continue-button"]').click()

    def test_ViewProducts(self, setup_class):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
        expected_url = "https://automationexercise.com/products"
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"
        view_product = driver.find_element(By.CSS_SELECTOR, 'a[href ="/product_details/1"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", view_product)
        view_product.click()
        expected_url = "https://automationexercise.com/product_details/1"
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_SearchProduct(self, setup_class):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
        expected_url = "https://automationexercise.com/products"
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"
        driver.find_element(By.ID, "search_product").send_keys("blue top")
        driver.find_element(By.ID, "submit_search").click()
        #driver.find_element(By.CLASS_NAME, "productinfo text-center")
        add = driver.find_element(By.CSS_SELECTOR, 'a[data-product-id="1"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", add)
        add.click()
        driver.find_element(By.CSS_SELECTOR, 'a[href = "/view_cart"]').click()
        driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()



            

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


def login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)


def add_item_to_cart(driver):
    item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    add_to_cart_button = item.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()
    time.sleep(5)


def verify_item_in_cart(driver):
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    cart_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    assert cart_item is not None
    time.sleep(5)


def logout(driver):
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()


def test_swag_labs(driver):
    # Verify SWAG LABS is present on the web page
    login(driver, USERNAME, PASSWORD)
    assert "Swag Labs" in driver.title

    # Add any one of the items to the cart
    add_item_to_cart(driver)

    # Verify the item is added to the cart
    verify_item_in_cart(driver)

    # Log out
    logout(driver)

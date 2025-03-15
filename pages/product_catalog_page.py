import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_item_to_cart(driver):
    item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    add_to_cart_button = item.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()
    time.sleep(5)


def logout(driver):
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()
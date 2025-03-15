import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def verify_item_in_cart(driver):
    cart_button = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
    cart_button.click()
    cart_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    assert cart_item is not None
    time.sleep(5)

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.run(order=3)
def test_add_to_cart(setup):
    driver = setup
    add_to_cart_item_webelement = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    add_to_cart_item = add_to_cart_item_webelement.text
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()

    # click on the cart symbol
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    item_added_to_cart_webelement = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
    item_added_to_cart = item_added_to_cart_webelement.text

    assert add_to_cart_item == item_added_to_cart


@pytest.mark.run(order=4)
def test_logout(setup):
    driver = setup
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.run(order=1)
def test_page_heading(setup):
    driver = setup
    page_heading = driver.find_element(By.CLASS_NAME, "login_logo")
    assert page_heading.text == "Swag Labs"


@pytest.mark.run(order=2)
def test_login(setup):
    driver = setup
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
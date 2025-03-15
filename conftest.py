import pytest
from selenium import webdriver

URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(50)
    driver.maximize_window()

    yield driver
    driver.close()

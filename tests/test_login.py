import os
import sys

import pytest

from pages.login import login, USERNAME, PASSWORD


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.run(order=1)
def test_login(driver):
    login(driver, USERNAME, PASSWORD)
    assert "Swag Labs" in driver.title

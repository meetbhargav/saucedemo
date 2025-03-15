import os
import sys

import pytest

from pages.cart_page import verify_item_in_cart
from pages.product_catalog_page import logout

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.run(order=3)
def test_cart_page(driver):

    # Verify the item is added to the cart
    verify_item_in_cart(driver)


@pytest.mark.run(order=4)
def test_logout(driver):
    # Log out
    logout(driver)
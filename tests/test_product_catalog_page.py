import os
import sys

import pytest

from pages.product_catalog_page import add_item_to_cart


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.run(order=2)
def test_product_catalog_page(driver):
    # Add any one of the items to the cart
    add_item_to_cart(driver)
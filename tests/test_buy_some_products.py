from playwright_tests_with_po.utils.random_data import generate_random_data
from playwright_tests_with_po.utils.choice_random_items import random_choice_items
import pytest


def test_add_and_verify_items(base_swag_lab, inventory, shopping_cart, checkout):

    all_items = inventory.inventory_items.count()
    random_items = random_choice_items(all_items, 3)

    inventory.add_items_to_cart(random_items)

    cart_items_details = inventory.get_items_details(random_items)

    base_swag_lab.shopping_cart.click()

    shopping_cart.checkout_button.click()

    first_name, last_name, zip_code = generate_random_data()

    checkout.fill_checkout_form(first_name, last_name, zip_code)

    checkout_items_details = checkout.get_items_details()

    total_price = checkout.get_total_price()

    total_price_with_tax = checkout.calculate_total_price_with_tax()

    assert total_price == pytest.approx(total_price_with_tax, 2)
    assert cart_items_details == checkout_items_details

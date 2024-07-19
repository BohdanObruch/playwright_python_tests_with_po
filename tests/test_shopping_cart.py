from playwright_tests_with_po.utils.choice_random_items import random_choice_items


def test_add_and_remove_product_from_the_cart(inventory, shopping_cart):

    inventory.add_item_to_cart_by_id(0)

    assert inventory.get_number_of_items_in_cart() == 1

    inventory.shopping_cart.click()

    assert shopping_cart.cart_items.count() >= 1

    shopping_cart.remove_cart_item_by_id(0)

    assert not shopping_cart.cart_items.is_visible()


def test_adding_random_items_to_the_shopping_cart(inventory, base_swag_lab, shopping_cart):
    all_items = inventory.inventory_items.count()
    random_items = random_choice_items(all_items, 3)

    inventory.add_items_to_cart(random_items)

    cart_items_details = inventory.get_items_details(random_items)

    base_swag_lab.shopping_cart.click()

    shopping_cart_items_details = shopping_cart.get_items_details()

    assert cart_items_details == shopping_cart_items_details

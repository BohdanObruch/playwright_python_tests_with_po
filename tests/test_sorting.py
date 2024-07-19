import pytest
from playwright_tests_with_po.utils.sorting import is_sorted_alphabetically, is_sorted_by_price


@pytest.mark.parametrize("option_text, sort_value, sort_function, is_descending, inventory_items_function_name", [
    ('Name (A to Z)', 'az', is_sorted_alphabetically, False, 'get_inventory_items_all_names'),
    ('Name (Z to A)', 'za', is_sorted_alphabetically, True, 'get_inventory_items_all_names'),
    ('Price (low to high)', 'lohi', is_sorted_by_price, False, 'get_inventory_items_all_prices'),
    ('Price (high to low)', 'hilo', is_sorted_by_price, True, 'get_inventory_items_all_prices'),
])
def test_sorting_by_(inventory, option_text, sort_value, sort_function, is_descending, inventory_items_function_name):
    inventory.sort_items_by(sort_value)

    assert inventory.get_active_option_text() == option_text

    inventory_items_function = getattr(inventory, inventory_items_function_name)
    items = inventory_items_function()

    assert sort_function(items, is_descending) is True

from .base_swag_lab_page import BaseSwagLabPage


class InventoryPage(BaseSwagLabPage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)

        self.url = '/inventory.html'
        self.header_title = self.page.locator('.title')
        self.inventory_items = self.page.locator('.inventory_item')
        self.add_item_to_cart_btns = self.page.locator('[id^="add-to-cart"]')
        self.inventory_items_name = self.page.locator('.inventory_item_name')
        self.inventory_items_price = self.page.locator('.inventory_item_price')
        self.inventory_items_description = self.page.locator('.inventory_item_desc')
        self.sort = self.page.locator('.product_sort_container')
        self.active_option = self.page.locator('.active_option')

    def sort_items_by(self, value):
        self.page.select_option('.product_sort_container', value)

    def get_active_option_text(self):
        return self.active_option.text_content()

    def add_item_to_cart_by_id(self, id):
        self.inventory_items.nth(id).locator(self.add_item_to_cart_btns).click()

    def get_inventory_items_all_prices(self):
        prices = self.inventory_items_price.all_text_contents()
        return [float(price.replace('$', '')) for price in prices]

    def get_inventory_items_all_names(self):
        names = self.inventory_items_name.all_text_contents()
        return [name.lower() for name in names]

    def get_inventory_items_all_descriptions(self):
        return self.inventory_items_description.all_text_contents()

    def get_inventory_items_prices(self, selected_items_indexes):
        prices = [self.inventory_items_price.nth(index).text_content() for index in selected_items_indexes]
        return [float(price.replace('$', '')) for price in prices]

    def get_inventory_items_names(self, selected_items_indexes):
        return [self.inventory_items_name.nth(index).text_content() for index in selected_items_indexes]

    def get_inventory_items_descriptions(self, selected_items_indexes):
        return [self.inventory_items_description.nth(index).text_content() for index in selected_items_indexes]

    def get_items_details(self, selected_items_indexes):
        details = [
            [name.strip().lower() for name in self.get_inventory_items_names(selected_items_indexes)],
            [description.strip() for description in
             self.get_inventory_items_descriptions(selected_items_indexes)],
            self.get_inventory_items_prices(selected_items_indexes),
        ]
        return [dict(zip(['name', 'description', 'price'], item)) for item in zip(*details)]

    def add_items_to_cart(self, selected_items_indexes):
        for index in selected_items_indexes:
            self.add_item_to_cart_by_id(index)

    def get_inventory_items_count(self):
        return self.inventory_items.count()

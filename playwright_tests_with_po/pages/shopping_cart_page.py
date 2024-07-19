from .base_swag_lab_page import BaseSwagLabPage


class ShoppingCartPage(BaseSwagLabPage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.url = '/cart.html'
        self.cart_items = self.page.locator('.cart_item')
        self.remove_item = self.page.locator('[id^="remove"]')
        self.items_name = self.page.locator('.inventory_item_name')
        self.items_price = self.page.locator('.inventory_item_price')
        self.items_description = self.page.locator('.inventory_item_desc')
        self.checkout_button = self.page.locator('#checkout')
        self.header_title = self.page.locator('.title')

    def get_cart_item(self):
        return self.cart_items

    def get_cart_item_by_name(self, name):
        return self.page.locator('.cart_item', has_text=name)

    def remove_cart_item_by_name(self, name):
        return self.get_cart_item_by_name(name).locator(self.remove_item)

    def remove_cart_item_by_id(self, id):
        return self.cart_items.nth(id).locator(self.remove_item).click()

    def get_items_all_prices(self):
        prices_elements = self.items_price.all_text_contents()
        prices = [float(price.replace('$', '')) for price in prices_elements]
        return prices

    def get_items_all_names(self):
        names_elements = self.items_name.all_text_contents()
        names = [name.lower() for name in names_elements]
        return names

    def get_items_all_descriptions(self):
        return self.items_description.all_text_contents()

    def get_items_details(self):
        names = self.get_items_all_names()
        descriptions = self.get_items_all_descriptions()
        prices = self.get_items_all_prices()
        return [{'name': name.strip().lower(), 'description': description.strip(), 'price': price}
                for name, description, price in zip(names, descriptions, prices)]

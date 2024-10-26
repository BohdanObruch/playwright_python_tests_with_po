from .base_page import BasePage


class BaseSwagLabPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.shopping_cart = page.locator('.shopping_cart_link')
        self.shopping_cart_badge = page.locator('.shopping_cart_badge')

    def get_number_of_items_in_cart(self):
        return int(self.shopping_cart_badge.text_content())

from .base_page import BasePage


class BaseSwagLabPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.shopping_cart = self.page.locator('.shopping_cart_link')
        self.shopping_cart_badge = self.page.locator('.shopping_cart_badge')

    def get_number_of_items_in_cart(self):
        return int(self.shopping_cart_badge.text_content())

from .shopping_cart_page import ShoppingCartPage


class CheckoutPage(ShoppingCartPage):
    def __init__(self, page):
        super().__init__(page)
        self.url = '/checkout-step-one.html'
        self.item_total_price = page.locator('[data-test="subtotal-label"]')
        self.tax_price = page.locator('[data-test="tax-label"]')
        self.total_price = page.locator('[data-test="total-label"]')
        self.first_name = page.locator('#first-name')
        self.last_name = page.locator('#last-name')
        self.zip_code = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')

    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)
        self.continue_button.click()

    def get_tax_price(self):
        tax_text = self.tax_price.text_content()
        tax_value = tax_text.replace('Tax: $', '')
        return float(tax_value)

    def get_item_total_price(self):
        item_total_text = self.item_total_price.text_content()
        item_total_value = item_total_text.replace('Item total: $', '')
        return float(item_total_value)

    def get_total_price(self):
        total_text = self.total_price.text_content()
        total_value = total_text.replace('Total: $', '')
        return float(total_value)

    def calculate_total_price_with_tax(self):
        item_total = self.get_item_total_price()
        tax = self.get_tax_price()
        return item_total + tax

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.user_name = self.page.locator('#user-name')
        self.password = self.page.locator('#password')
        self.login_btn = self.page.locator('#login-button')

    def perform_login(self, user_name, password):
        self.user_name.fill(user_name)
        self.password.fill(password)
        self.login_btn.click()

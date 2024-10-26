from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.user_name = page.locator('#user-name')
        self.password = page.locator('#password')
        self.login_btn = page.locator('#login-button')

    def perform_login(self, user_name, password):
        self.user_name.fill(user_name)
        self.password.fill(password)
        self.login_btn.click()

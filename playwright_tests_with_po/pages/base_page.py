from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = base_url

    def get_url(self):
        return self.page.url

    def navigate(self):
        self.page.goto(self.url)

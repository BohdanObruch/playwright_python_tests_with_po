from typing import Generator

import pytest
from playwright.sync_api import Page, BrowserContext
from playwright_tests_with_po.pages.login_page import LoginPage
from playwright_tests_with_po.pages.inventory_page import InventoryPage
from playwright_tests_with_po.pages.shopping_cart_page import ShoppingCartPage
from playwright_tests_with_po.pages.base_swag_lab_page import BaseSwagLabPage
from playwright_tests_with_po.pages.checkout_page import CheckoutPage

from playwright_tests_with_po.test_data.credentials import standard_user


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(autouse=True)
def page(page:Page):
    yield page
    page.close()



@pytest.fixture
def login(page):
    return LoginPage(page)


@pytest.fixture
def inventory(page):
    return InventoryPage(page)


@pytest.fixture
def shopping_cart(page):
    return ShoppingCartPage(page)


@pytest.fixture
def base_swag_lab(page):
    return BaseSwagLabPage(page)


@pytest.fixture
def checkout(page):
    return CheckoutPage(page)


@pytest.fixture(autouse=True)
def authorizations(login):
    login.navigate()
    login.perform_login(standard_user['username'], standard_user['password'])

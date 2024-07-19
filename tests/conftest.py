import pytest

from playwright_tests_with_po.pages.login_page import LoginPage
from playwright_tests_with_po.pages.inventory_page import InventoryPage
from playwright_tests_with_po.pages.shopping_cart_page import ShoppingCartPage
from playwright_tests_with_po.pages.base_swag_lab_page import BaseSwagLabPage
from playwright_tests_with_po.pages.checkout_page import CheckoutPage

from playwright_tests_with_po.test_data.credentials import standard_user


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://www.saucedemo.com/", help="url to test")


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        viewport={'width': 1280, 'height': 1024}

    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def login(page, base_url):
    return LoginPage(page, base_url)


@pytest.fixture
def inventory(page, base_url):
    return InventoryPage(page, base_url)


@pytest.fixture
def shopping_cart(page, base_url):
    return ShoppingCartPage(page, base_url)


@pytest.fixture
def base_swag_lab(page, base_url):
    return BaseSwagLabPage(page, base_url)


@pytest.fixture
def checkout(page, base_url):
    return CheckoutPage(page, base_url)


@pytest.fixture(autouse=True)
def authorizations(login):
    login.navigate()
    login.perform_login(standard_user['username'], standard_user['password'])

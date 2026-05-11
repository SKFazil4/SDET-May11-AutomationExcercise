import pytest
from playwright.sync_api import Playwright, Page
from pages.home_page import Home
from pages.login_page import Login
from pages.product_page import Product
from pages.signup_page import SignUp
from pages.cart_page import Cart
from pages.product_deatils_page import ProductDetail
from pages.checkout_page import Checkout
from pages.payment_page import Payment

@pytest.fixture
def page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()

@pytest.fixture
def home_page(page:Page):
    yield Home(page)

@pytest.fixture
def login_page(page:Page):
    yield Login(page)

@pytest.fixture
def product_page(page:Page):
    yield Product(page)

@pytest.fixture
def signup_page(page:Page):
    yield SignUp(page)

@pytest.fixture
def cart_page(page:Page):
    yield Cart(page)

@pytest.fixture
def product_details_page(page:Page):
    yield ProductDetail(page)

@pytest.fixture
def checkout_page(page:Page):
    yield Checkout(page)

@pytest.fixture
def payment_page(page:Page):
    yield Payment(page)

@pytest.fixture
def context():
    return {}
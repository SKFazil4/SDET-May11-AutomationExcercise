from playwright.sync_api import Page, expect
from utils.config import BASE_URL
import random

class Home:
    def __init__(self, page:Page):
        self.page = page

    def navigate_to_home(self):
        self.page.goto(BASE_URL)

    def click_on_link_with_name(self, link_name:str):
        self.page.get_by_role("link", name=link_name).click()

    def click_on_button_with_name(self, btn_name:str):
        self.page.get_by_role("button", name=btn_name).click()

    def verify_text_visibility(self, text:str):
        expect(self.page.get_by_text(text)).to_be_visible()

    def click_view_product(self):
        products = self.page.locator(".features_items .product-image-wrapper")
        random_num = random.randint(0,products.count()-1)
        products.nth(random_num).get_by_role("link", name="View Product").click()

    def add_random_products(self):
        products = self.page.locator(".features_items .single-products")
        for i in range(1):
            random_num = random.randint(0, products.count() - 1)
            product = products.nth(random_num)
            product.hover()
            product.locator(".product-overlay .add-to-cart").click()
            expect(self.page.get_by_text("Continue Shopping")).to_be_visible()
            self.click_on_button_with_name("Continue Shopping")
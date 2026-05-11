from playwright.sync_api import Page, expect

class ProductDetail:
    def __init__(self, page:Page):
        self.page = page

    def check_product_details_page_open(self):
        assert "product_details" in self.page.url

    def increase_quantity(self, quantity:str):
        self.page.locator("#quantity").fill(quantity)

    def click_on_link_with_name(self, link_name: str):
        self.page.get_by_role("link", name=link_name).click()

    def click_on_button_with_name(self, btn_name: str):
        self.page.get_by_role("button", name=btn_name).click()

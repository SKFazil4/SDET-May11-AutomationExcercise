from playwright.sync_api import Page, expect

class Checkout:
    def __init__(self, page:Page):
        self.page = page

    def click_on_link_with_name(self, link_name: str):
        self.page.get_by_role("link", name=link_name).click()

    def check_products_is_present(self):
        products_count = self.page.locator("#cart_info tbody tr").count()
        assert products_count >= 1

    def fill_comment_description(self, description:str):
        self.page.locator("#ordermsg textarea").fill(description)
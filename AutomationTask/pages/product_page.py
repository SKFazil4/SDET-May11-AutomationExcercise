from playwright.sync_api import Page, expect

class Product:
    def __init__(self, page:Page):
        self.page = page

    def verify_text_visibility(self, text:str):
        expect(self.page.get_by_text(text)).to_be_visible()

    def fill_search_box(self, search_input:str):
        self.page.locator("#search_product").fill(search_input)

    def click_on_search_btn(self):
        self.page.locator("#submit_search").click()

    def click_on_link_with_name(self, link_name:str):
        self.page.get_by_role("link", name=link_name).click()

    def click_on_button_with_name(self, btn_name:str):
        self.page.get_by_role("button", name=btn_name).click()

    def look_for_search_input_text(self, input_txt:str):
        products_names = self.page.locator(".productinfo p").all_text_contents()
        for product_name in products_names:
            assert input_txt.lower() in product_name.lower()

    def hover_over_particular_product(self, product_num:int):
        product = self.page.locator(".single-products").nth(product_num-1)
        product.hover()
        product.locator(".product-overlay .add-to-cart").click()

    def wait_for_some_time(self):
        self.page.wait_for_timeout(8000)
from playwright.sync_api import Page, expect

class Cart:
    def __init__(self, page:Page):
        self.page = page

    def verify_no_of_products(self, products_num:int):
        products_count = self.page.locator("#cart_info_table tbody tr").count()
        assert products_count == products_num

    def verify_products_total_price(self):
        products = self.page.locator("#cart_info_table tbody tr")
        for i in range(products.count()):
            product = products.nth(i)
            price = product.locator(".cart_price p").text_content()
            price = int(price.split(" ")[1])
            quantity = product.locator(".cart_quantity button").text_content()
            quantity = int(quantity)
            total_price = product.locator(".cart_total p").text_content()
            total_price = int(total_price.split(" ")[1])
            assert price*quantity == total_price

    def verify_product_quantity(self, quantity:int):
        el_quantity = self.page.locator("tr .cart_quantity button").text_content()
        assert quantity == int(el_quantity)

    def check_cart_page_open(self):
        assert "view_cart" in self.page.url

    def click_on_link_with_name(self, link_name: str):
        self.page.get_by_role("link", name=link_name).click()

    def click_proceed_to_checkout(self):
        self.page.locator(".check_out").click()

    def remove_product_in_cart(self):
        product = self.page.locator("#cart_info_table tbody").nth(0)
        product_name = product.locator(".cart_description h4").text_content()
        product.locator(".cart_quantity_delete").click()
        return product_name

    def check_product_existence(self, product_name:str):
        expect(self.page.get_by_text(product_name)).not_to_be_visible()

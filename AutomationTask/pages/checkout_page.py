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

    def validate_total_price_per_product(self):
        products = self.page.locator("#cart_info tbody tr")
        products_count = products.count()-1
        assert products_count >= 1
        total_product_price = 0
        for i in range(products_count):
            product_price = products.nth(i).locator(".cart_price p").text_content()
            product_price = int(product_price.split(" ")[1])
            product_quantity = products.nth(i).locator(".cart_quantity button").text_content()
            product_quantity = int(product_quantity)
            product_total_price = products.nth(i).locator(".cart_total p").text_content()
            product_total_price = int(product_total_price.split(" ")[1])
            assert product_price*product_quantity == product_total_price
            total_product_price += product_total_price
        return total_product_price

    def validate_total_products_amount(self, products_total_price:int):
        total_row = self.page.locator("#cart_info tbody tr").last
        total_amount = total_row.locator("td p").text_content()
        total_amount = int(total_amount.split(" ")[1])
        assert total_amount == products_total_price
from playwright.sync_api import Page

class Payment:
    def __init__(self, page:Page):
        self.page = page

    def fill_payment_details(self, data_id:str, pay_details:str):
        self.page.locator(f'input[data-qa={data_id}]').fill(pay_details)

    def click_on_button_with_name(self, btn_name:str):
        self.page.get_by_role("button", name=btn_name).click()
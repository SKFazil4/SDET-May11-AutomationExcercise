from playwright.sync_api import Page, expect

class SignUp:
    def __init__(self, page:Page):
        self.page = page

    def verify_text_visibility(self, text:str):
        expect(self.page.get_by_text(text)).to_be_visible()

    def click_radio_btn_by_value(self, item_value:str):
        self.page.locator(f'input[type="radio"][value={item_value}]').check()

    def fill_data_input_text_by_id(self, element_id:str, text_data:str):
        self.page.locator(f"#{element_id}").fill(text_data)

    def select_option_by_id(self, select_id:str, option_label:str):
        self.page.locator(f"#{select_id}").select_option(label=option_label)

    def click_checkbox_by_id(self, element_id):
        self.page.locator(f"#{element_id}").check()

    def click_on_button_with_name(self, btn_name:str):
        self.page.get_by_role("button", name=btn_name).click()
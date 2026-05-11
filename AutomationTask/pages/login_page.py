from playwright.sync_api import Page, expect
from utils.config import BASE_URL

class Login:
    def __init__(self, page:Page):
        self.page = page

    def navigate_to_home(self):
        self.page.goto(BASE_URL)

    def click_on_button_with_name(self, btn_name:str):
        self.page.get_by_role("button", name=btn_name).click()

    def verify_text_visibility(self, text:str):
        expect(self.page.get_by_text(text)).to_be_visible()

    def enter_signup_name(self, name:str):
        self.page.locator('[data-qa="signup-name"]').fill(name)

    def enter_signup_email(self,email:str):
        self.page.locator('[data-qa="signup-email"]').fill(email)

    def enter_login_email(self, email:str):
        self.page.locator('[data-qa="login-email"]').fill(email)

    def enter_login_password(self,password:str):
        self.page.locator('[data-qa="login-password"]').fill(password)

    def wait_for_some_time(self):
        self.page.wait_for_timeout(3000)
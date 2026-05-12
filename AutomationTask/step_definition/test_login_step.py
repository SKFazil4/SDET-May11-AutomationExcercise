from pytest_bdd import given, when, then, parsers, scenarios
from pages.login_page import Login
from pages.home_page import Home
from pages.signup_page import SignUp
from _pytest.fixtures import FixtureRequest

scenarios("../features/login.feature")

# Home Page
@given("Browser launch")
def launch_browser(home_page:Home):
    pass

@when("Navigated to home page")
def navigate_to_home_page(home_page:Home):
    home_page.navigate_to_home()

@then(parsers.parse('Verify "{text_display}" is visible in "{page_name:w}"'))
def find_out_the_given_text_in_home(request:FixtureRequest,text_display:str, page_name:str):
    page_obj = request.getfixturevalue(page_name)
    page_obj.verify_text_visibility(text_display)

@when(parsers.parse('Click on "{link_name}" link from "{page_name:w}"'))
def when_click_on_link_from_home(request:FixtureRequest, page_name:str, link_name:str):
    page_obj = request.getfixturevalue(page_name)
    page_obj.click_on_link_with_name(link_name)

# Login Page
@given(parsers.parse('SignUp name "{user_name}"'))
def enter_signup_name_value(login_page:Login, user_name:str):
    login_page.enter_signup_name(user_name)

@given(parsers.parse('SignUp email "{user_email}"'))
def enter_signup_email_value(login_page:Login, user_email:str):
    login_page.enter_signup_email(user_email)

@when(parsers.parse('Click on "{btn_name}" button in "{page_name:w}"'))
def when_click_on_button(request:FixtureRequest, page_name:str, btn_name:str):
    page_obj = request.getfixturevalue(page_name)
    page_obj.click_on_button_with_name(btn_name)

# SignUp Page

@given(parsers.parse('Check on title whose value "{title_val}"'))
def check_on_title_name(signup_page:SignUp, title_val:str):
    signup_page.click_radio_btn_by_value(title_val)

@given("Fill the following fields")
def fill_text_data_in_element(signup_page:SignUp, datatable:list):
    for row in datatable:
        element_id = row[0]
        value = row[1]
        signup_page.fill_data_input_text_by_id(element_id, value)

@given("Select the following fields")
def select_option_using_id_and_value(signup_page:SignUp, datatable:list):
    for row in datatable:
        element_id = row[0]
        value = row[1]
        signup_page.select_option_by_id(element_id, value)


@given(parsers.parse('Checkbox with checkbox id "{checkbox_id}"'))
def check_checkbox_by_its_id(signup_page:SignUp, checkbox_id:str):
    signup_page.click_checkbox_by_id(checkbox_id)

# Wait Time
@given("Wait for 3 seconds")
def wait_time(login_page:Login):
    login_page.wait_for_some_time()

#Login Page
@given(parsers.parse('Login email "{user_email}"'))
def enter_login_email_value(login_page:Login, user_email:str):
    login_page.enter_login_email(user_email)

@given(parsers.parse('Login password "{user_password}"'))
def enter_login_password_value(login_page:Login, user_password:str):
    login_page.enter_login_password(user_password)
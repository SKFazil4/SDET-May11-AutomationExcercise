import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from _pytest.fixtures import FixtureRequest
from pages.home_page import Home
from pages.login_page import Login
from pages.signup_page import SignUp
from pages.product_page import Product
from pages.cart_page import Cart
from pages.product_deatils_page import ProductDetail
from pages.checkout_page import Checkout
from pages.payment_page import Payment

scenarios("../features/product.feature")

#Home Page
@given("Browser launch")
def launch_browser(home_page:Home):
    pass

@when("Navigated to home page")
def navigate_to_home_page(home_page:Home):
    home_page.navigate_to_home()

@then(parsers.parse('Verify "{text_display}" is visible in "{page_name:w}"'))
def find_out_the_given_text_in_home(request:FixtureRequest, page_name:str, text_display:str):
    page_object = request.getfixturevalue(page_name)
    page_object.verify_text_visibility(text_display)

@when(parsers.parse('Click on "{link_name}" link from "{page_name:w}"'))
@then(parsers.parse('Click on "{link_name}" link from "{page_name:w}"'))
def when_click_on_link_button_in_home(request:FixtureRequest, page_name:str, link_name:str):
    page_object = request.getfixturevalue(page_name)
    page_object.click_on_link_with_name(link_name)

@given("Click view product for any product")
def click_view_product_for_any_product(home_page:Home):
    home_page.click_view_product()

@given("Add products to cart")
def add_products_to_cart(home_page:Home):
    home_page.add_random_products()

# Login Page
@given(parsers.parse('SignUp name "{user_name}"'))
def enter_signup_name_value(login_page:Login, user_name:str):
    login_page.enter_signup_name(user_name)

@given(parsers.parse('SignUp email "{user_email}"'))
def enter_signup_email_value(login_page:Login, user_email:str):
    login_page.enter_signup_email(user_email)

@given(parsers.parse('Login email "{user_email}"'))
def enter_login_email_value(login_page:Login, user_email:str):
    login_page.enter_login_email(user_email)

@given(parsers.parse('Login password "{user_password}"'))
def enter_login_password_value(login_page:Login, user_password:str):
    login_page.enter_login_password(user_password)

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

#Product Page
@when(parsers.parse('Enter product name "{search_input}" in search box'))
def enter_product_name_in_search_box(product_page:Product, search_input):
    product_page.fill_search_box(search_input)

@when("Click on Search button")
def click_on_search_button(product_page:Product):
    product_page.click_on_search_btn()

@then(parsers.parse('Check for products with name "{search_input}" exist in products'))
def check_products_availability(product_page:Product, search_input:str):
    product_page.look_for_search_input_text(search_input)

@when(parsers.parse('Hover over product {product_num:d} and click add to cart'))
def hover_over_product_and_add_to_cart(product_page:Product, product_num:int):
    product_page.hover_over_particular_product(product_num)

@when(parsers.parse('Click on "{btn_name}" button in "{page_name:w}"'))
@then(parsers.parse('Click on "{btn_name}" button in "{page_name:w}"'))
def click_on_button_in_product_page(request:FixtureRequest,page_name:str, btn_name:str):
    page_obj = request.getfixturevalue(page_name)
    page_obj.click_on_button_with_name(btn_name)

#Cart page
@then(parsers.parse('Verify {products_num:d} products added to cart'))
def check_for_products_count(cart_page:Cart,products_num:int):
    cart_page.verify_no_of_products(products_num)

@then("Verify total price with product price and quantity")
def validate_total_price_of_products(cart_page:Cart):
    cart_page.verify_products_total_price()

@then(parsers.parse('Verify product quantity is {quantity:d}'))
def validate_product_quantity(cart_page:Cart, quantity:int):
    cart_page.verify_product_quantity(quantity)

@then("Verify cart page is opened")
def verify_cart_page_opened(cart_page:Cart):
    cart_page.check_cart_page_open()

@then("Click on Proceed to checkout button")
def click_on_proceed_to_checkout(cart_page:Cart):
    cart_page.click_proceed_to_checkout()

@when("Product is removed from the cart")
def remove_product_from_cart(cart_page:Cart, context:dict):
    context["product_name"] = cart_page.remove_product_in_cart()

@then("Verify product is removed from the cart")
def verify_product_is_present_in_cart(cart_page:Cart, context:dict):
    product_name = context["product_name"]
    cart_page.check_product_existence(product_name)

#ProductDetails Page
@then("Verify product details is opened")
def verify_product_details_are_open(product_details_page:ProductDetail):
    product_details_page.check_product_details_page_open()

@given(parsers.parse('Increase quantity to "{quantity}"'))
def increase_product_quantity(product_details_page:ProductDetail, quantity:str):
    product_details_page.increase_quantity(quantity)

#Checkout Page
@then("Verify product is present")
def verify_product_is_present(checkout_page:Checkout):
    checkout_page.check_products_is_present()

@given(parsers.parse('Enter description in comment text area "{description}"'))
def enter_description_in_comment(checkout_page:Checkout,description:str):
    checkout_page.fill_comment_description(description)

@then("Validate the total price of each products based on their quantity")
def validate_total_price_for_each_product(checkout_page:Checkout, context:dict):
    context["products_total_price"] = checkout_page.validate_total_price_per_product()

@then("Validate the total amount of all the products")
def validate_total_price_of_all_products(checkout_page:Checkout, context:dict):
    products_total_price = context["products_total_price"]
    checkout_page.validate_total_products_amount(products_total_price)

#Payment Page
@given(parsers.parse('Enter payment details "{input_data}" using "{data_id}"'))
def enter_payment_details(payment_page:Payment, input_data:str, data_id:str):
    payment_page.fill_payment_details(data_id, input_data)

# Wait Time
@given("Wait for sometime")
def wait_time(product_page:Product):
    product_page.wait_for_some_time()

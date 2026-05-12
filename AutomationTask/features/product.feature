Feature: Product Page
  @task9
  Scenario: Search Product
    #Home Page
    Given Browser launch
    When Navigated to home page
    Then Verify "Home" is visible in "home_page"
    When Click on "Products" link from "home_page"
    #Product Page
    Then Verify "All Products" is visible in "product_page"
    When Enter product name "Blue" in search box
    When Click on Search button
    Then Verify "Searched Products" is visible in "product_page"
    Then Check for products with name "Blue" exist in products

  @task12
  Scenario: Add Products in Cart
    #Home Page
    Given Browser launch
    When Navigated to home page
    Then Verify "Home" is visible in "home_page"
    When Click on "Products" link from "home_page"
    #Product Page
    When Hover over product 1 and click add to cart
    Then Click on "Continue Shopping" button in "product_page"
    When Hover over product 2 and click add to cart
    Then Click on "View Cart" link from "product_page"
    #Cart Page
    Then Verify 2 products added to cart
    Then Verify total price with product price and quantity

  @task13
  Scenario: Verify Product quantity in Cart
    #Home Page
    Given Browser launch
    When Navigated to home page
    Then Verify "Home" is visible in "home_page"
    Given Click view product for any product
    #ProductDetails Page
    Then Verify product details is opened
    Given Increase quantity to "4"
    Then Click on "Add to cart" button in "product_details_page"
    Then Click on "View Cart" link from "product_details_page"
    #Cart Page
    Then Verify product quantity is 4

  @task14
  Scenario: Place Order Register while Checkout
    #Home Page
    Given Browser launch
    When Navigated to home page
    Then Verify "Home" is visible in "home_page"
    Given Add products to cart
    When Click on "Cart" link from "home_page"
    #Cart Page
    Then Verify cart page is opened
    Then Click on Proceed to checkout button
    Then Click on "Register / Login" link from "cart_page"
    #Login Page
    Then Verify "New User Signup!" is visible in "login_page"
    Given SignUp name "Fazil"
    Given SignUp email "fazil@gmail.com"
    When Click on "Signup" button in "login_page"
    #SignUp Page
    Then Verify "ENTER ACCOUNT INFORMATION" is visible in "signup_page"
    Given Check on title whose value "Mr"
    Given Select the following fields
    |days|11|
    |months|December|
    |years|2002|
    |country|India|
    Given Checkbox with checkbox id "newsletter"
    Given Checkbox with checkbox id "optin"
    Given Fill the following fields
    |first_name| Gime|
    |last_name|Doe|
    |password|Fazil@123|
    |company|Sutherland|
    |address1|Manikonda|
    |address2|Lanco Hills|
    |state|Telangana|
    |city|Hyderabad|
    |zipcode|500032|
    |mobile_number|9876543210|
    When Click on "Create Account" button in "signup_page"
    #Home Page
    Then Verify "ACCOUNT CREATED!" is visible in "home_page"
    When Click on "Continue" link from "home_page"
    Then Verify "Logged in as Fazil" is visible in "home_page"
    When Click on "Cart" link from "home_page"
    #Cart Page
    Then Click on Proceed to checkout button
    #Checkout Page
    Then Verify product is present
    Given Enter description in comment text area "Please deliver asap"
    When Click on "Place Order" link from "checkout_page"
    #Payment Page
    Given Enter payment details "Fazil Shaik" using "name-on-card"
    Given Enter payment details "241011121124" using "card-number"
    Given Enter payment details "241" using "cvc"
    Given Enter payment details "11" using "expiry-month"
    Given Enter payment details "2028" using "expiry-year"
    When Click on "Pay and Confirm Order" button in "payment_page"
    #Home Page
    Then Verify "Congratulations! Your order has been confirmed!" is visible in "home_page"
    When Click on "Continue" link from "home_page"
    When Click on "Delete Account" link from "home_page"
    Then Verify "ACCOUNT DELETED!" is visible in "home_page"
    When Click on "Continue" link from "home_page"

  @task17
  Scenario: Remove Products From Cart
    #Home Page
    Given Browser launch
    When Navigated to home page
    Then Verify "Home" is visible in "home_page"
    Given Add products to cart
    When Click on "Cart" link from "home_page"
    #Cart Page
    Then Verify cart page is opened
    When Product is removed from the cart
    Then Verify product is removed from the cart

  @task01_12_05_2026
  Scenario: Add products and check total amount
    #Home Page
    Given Browser launch
    When Navigated to home page
    Then Verify "Home" is visible in "home_page"
    When Click on "Signup / Login" link from "home_page"
    #Login Page
    Then Verify "Login to your account" is visible in "login_page"
    Given Login email "fazil@gmail.com"
    Given Login password "Fazil@123"
    When Click on "Login" button in "login_page"
    #Home Page
    Then Verify "Logged in as Fazil" is visible in "home_page"
    Given Click view product for any product
    #ProductDetails Page
    Then Verify product details is opened
    Given Increase quantity to "4"
    Then Click on "Add to cart" button in "product_details_page"
    Then Click on "Continue Shopping" button in "product_details_page"
    Then Click on "Home" link from "product_details_page"
    #Home Page
    Given Click view product for any product
    #ProductDetails Page
    Then Verify product details is opened
    Given Increase quantity to "4"
    Then Click on "Add to cart" button in "product_details_page"
    Then Click on "Continue Shopping" button in "product_details_page"
    Then Click on "Home" link from "product_details_page"
    #Home Page
    Given Click view product for any product
    #ProductDetails Page
    Then Verify product details is opened
    Given Increase quantity to "4"
    Then Click on "Add to cart" button in "product_details_page"
    Then Click on "View Cart" link from "product_details_page"
    #Cart Page
    Then Click on Proceed to checkout button
    #Checkout Page
    Then Verify product is present
    Then Validate the total price of each products based on their quantity
    Then Validate the total amount of all the products
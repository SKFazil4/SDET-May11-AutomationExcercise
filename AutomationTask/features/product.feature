Feature: Product Page
#  #Task 9
#  Scenario: Search Product
#    #Home Page
#    Given Browser launch
#    When Navigated to home page
#    Then Verify "Home" is visible in "home_page"
#    When Click on "Products" link from "home_page"
#    #Product Page
#    Then Verify "All Products" is visible in "product_page"
#    When Enter product name "Blue" in search box
#    When Click on Search button
#    Then Verify "Searched Products" is visible in "product_page"
#    Then Check for products with name "Blue" exist in products
#
#  #Task 12
#  Scenario: Add Products in Cart
#    #Home Page
#    Given Browser launch
#    When Navigated to home page
#    Then Verify "Home" is visible in "home_page"
#    When Click on "Products" link from "home_page"
#    #Product Page
#    When Hover over product 1 and click add to cart
#    Then Click on "Continue Shopping" button in "product_page"
#    When Hover over product 2 and click add to cart
#    Then Click on "View Cart" link from "product_page"
#    #Cart Page
#    Then Verify 2 products added to cart
#    Then Verify total price with product price and quantity
#
#  #Task 13
#  Scenario: Verify Product quantity in Cart
#    #Home Page
#    Given Browser launch
#    When Navigated to home page
#    Then Verify "Home" is visible in "home_page"
#    Given Click view product for any product
#    #ProductDetails Page
#    Then Verify product details is opened
#    Given Increase quantity to "4"
#    Then Click on "Add to cart" button in "product_details_page"
#    Then Click on "View Cart" link from "product_details_page"
#    #Cart Page
#    Then Verify product quantity is 4
#    Given Wait for sometime

#  Task 14
#  Scenario: Place Order Register while Checkout
#    #Home Page
#    Given Browser launch
#    When Navigated to home page
#    Then Verify "Home" is visible in "home_page"
#    Given Add products to cart
#    When Click on "Cart" link from "home_page"
#    #Cart Page
#    Then Verify cart page is opened
#    Then Click on Proceed to checkout button
#    Then Click on "Register / Login" link from "cart_page"
#    #Login Page
#    Then Verify "New User Signup!" is visible in "login_page"
#    Given SignUp name "Fazil"
#    Given SignUp email "fazil@gmail.com"
#    When Click on "Signup" button in "login_page"
#    #SignUp Page
#    Then Verify "ENTER ACCOUNT INFORMATION" is visible in "signup_page"
#    Given Check on title whose value "Mr"
#    Given Fill "Fazil@123" in the element id "password"
#    Given Select from select id "days" with option value "11"
#    Given Select from select id "months" with option value "December"
#    Given Select from select id "years" with option value "2002"
#    Given Checkbox with checkbox id "newsletter"
#    Given Checkbox with checkbox id "optin"
#    Given Fill "Fazil" in the element id "first_name"
#    Given Fill "Shaik" in the element id "last_name"
#    Given Fill "Sutherland" in the element id "company"
#    Given Fill "Manikonda" in the element id "address1"
#    Given Fill "Lanco Hills" in the element id "address2"
#    Given Select from select id "country" with option value "India"
#    Given Fill "Telangana" in the element id "state"
#    Given Fill "Hyderabad" in the element id "city"
#    Given Fill "500032" in the element id "zipcode"
#    Given Fill "9876543210" in the element id "mobile_number"
#    When Click on "Create Account" button in "signup_page"
#    #Home Page
#    Then Verify "ACCOUNT CREATED!" is visible in "home_page"
#    When Click on "Continue" link from "home_page"
#    Then Verify "Logged in as Fazil" is visible in "home_page"
#    When Click on "Cart" link from "home_page"
#    #Cart Page
#    Then Click on Proceed to checkout button
#    #Checkout Page
#    Then Verify product is present
#    Given Enter description in comment text area "Please deliver asap"
#    When Click on "Place Order" link from "checkout_page"
#    #Payment Page
#    Given Enter payment details "Fazil Shaik" using "name-on-card"
#    Given Enter payment details "241011121124" using "card-number"
#    Given Enter payment details "241" using "cvc"
#    Given Enter payment details "11" using "expiry-month"
#    Given Enter payment details "2028" using "expiry-year"
##    Given Wait for sometime
#    When Click on "Pay and Confirm Order" button in "payment_page"
#    #Home Page
#    Then Verify "Congratulations! Your order has been confirmed!" is visible in "home_page"
#    When Click on "Continue" link from "home_page"
#    When Click on "Delete Account" link from "home_page"
#    Then Verify "ACCOUNT DELETED!" is visible in "home_page"
#    When Click on "Continue" link from "home_page"

  #Task 17
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
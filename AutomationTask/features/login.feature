Feature: Login Page
  @task1
  Scenario: Register User
    #Home Page
    Given Browser launch
    When Navigated to home page
    Then Verify "Home" is visible in "home_page"
    When Click on "Signup / Login" link from "home_page"
    #Login Page
    Then Verify "New User Signup!" is visible in "login_page"
    Given SignUp name "Fazil"
    Given SignUp email "fazil@gmail.com"
    When Click on "Signup" button in "login_page"
    #SignUp Page
    Then Verify "ENTER ACCOUNT INFORMATION" is visible in "signup_page"
    Given Check on title whose value "Mr"
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
    Given Checkbox with checkbox id "newsletter"
    Given Checkbox with checkbox id "optin"
    Given Select the following fields
    |days|11|
    |months|December|
    |years|2002|
    |country|India|
    When Click on "Create Account" button in "signup_page"
    #Home Page
    Then Verify "ACCOUNT CREATED!" is visible in "home_page"
    When Click on "Continue" link from "home_page"
    Then Verify "Logged in as Fazil" is visible in "home_page"
    When Click on "Delete Account" link from "home_page"
    Then Verify "ACCOUNT DELETED!" is visible in "home_page"
    When Click on "Continue" link from "home_page"

  @task2
  Scenario:  Login User with correct email and password
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
    When Click on "Delete Account" link from "home_page"
    Then Verify "ACCOUNT DELETED!" is visible in "home_page"
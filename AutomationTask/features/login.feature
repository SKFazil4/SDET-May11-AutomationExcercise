Feature: Login Page
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
    Given Fill "Fazil@123" in the element id "password"
    Given Select from select id "days" with option value "11"
    Given Select from select id "months" with option value "December"
    Given Select from select id "years" with option value "2002"
    Given Checkbox with checkbox id "newsletter"
    Given Checkbox with checkbox id "optin"
    Given Fill "Fazil" in the element id "first_name"
    Given Fill "Shaik" in the element id "last_name"
    Given Fill "Sutherland" in the element id "company"
    Given Fill "Manikonda" in the element id "address1"
    Given Fill "Lanco Hills" in the element id "address2"
    Given Select from select id "country" with option value "India"
    Given Fill "Telangana" in the element id "state"
    Given Fill "Hyderabad" in the element id "city"
    Given Fill "500032" in the element id "zipcode"
    Given Fill "9876543210" in the element id "mobile_number"
    When Click on "Create Account" button in "signup_page"
    #Home Page
    Then Verify "ACCOUNT CREATED!" is visible in "home_page"
    When Click on "Continue" link from "home_page"
    Then Verify "Logged in as Fazil" is visible in "home_page"
    When Click on "Delete Account" link from "home_page"
    Then Verify "ACCOUNT DELETED!" is visible in "home_page"
    When Click on "Continue" link from "home_page"

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
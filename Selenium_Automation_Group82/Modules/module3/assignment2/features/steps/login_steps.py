from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("I open the login page")
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://the-internet.herokuapp.com/login")


@when('I enter username "{username}"')
def enter_username(context, username):
    context.driver.find_element(By.ID, "username").send_keys(username)


@when('I enter password "{password}"')
def enter_password(context, password):
    context.driver.find_element(By.ID, "password").send_keys(password)


@when("I click the login button")
def click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


@then('I should get "{result}"')
def verify_login(context, result):

    if result == "success":
        assert "/secure" in context.driver.current_url
    else:
        assert "/login" in context.driver.current_url

    context.driver.quit()
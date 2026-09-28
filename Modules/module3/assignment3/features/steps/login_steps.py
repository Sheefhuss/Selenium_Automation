from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

@given("I open the login page")
def open_login_page(context):
    # Uses the dynamic URL loaded from config.ini via environment.py
    context.driver.get(context.base_url)
    context.login = LoginPage(context.driver)

@when('I enter username "{username}"')
def enter_username(context, username):
    context.login.enter_username(username)

@when('I enter password "{password}"')
def enter_password(context, password):
    context.login.enter_password(password)

@when("I click the login button")
def click_login(context):
    context.login.click_login()

@then("I should be successfully logged in")
def verify_login(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/secure")
    )
    assert "/secure" in context.driver.current_url
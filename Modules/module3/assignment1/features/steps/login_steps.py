from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("I open the login page")
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://the-internet.herokuapp.com/login")


@when('I enter username "tomsmith"')
def enter_username(context):
    context.driver.find_element(By.ID, "username").send_keys("tomsmith")


@when('I enter password "SuperSecretPassword!"')
def enter_password(context):
    context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")


@when("I click the login button")
def click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


@then("I should be successfully logged in")
def verify_login(context):
    assert "/secure" in context.driver.current_url
    context.driver.quit()
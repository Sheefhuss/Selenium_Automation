from selenium import webdriver
from login_page import LoginPage


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)#login is an object of LoginPage

    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    assert "/secure" in driver.current_url

    driver.quit()
test_login()
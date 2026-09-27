import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()

def read_test_data():
    with open("modules/module2/login_data.csv", "r") as file:
        return list(csv.DictReader(file))

@pytest.mark.parametrize("data", read_test_data())
def test_login(driver, data):

    driver.find_element(
        By.ID, "username"
    ).send_keys(data["username"])

    driver.find_element(
        By.ID, "password"
    ).send_keys(data["password"])

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    if data["expected"] == "success":

        assert "/secure" in driver.current_url

    else:

        assert "/login" in driver.current_url
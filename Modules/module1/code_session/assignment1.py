from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.saucedemo.com/")

    # Locate the username field by its id attribute
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    # Locate the password field by its name attribute
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("secret_sauce")

    # Locate the login button by an XPath expression
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_button.click()

    time.sleep(1)

    current_url = driver.current_url
    assert "/inventory.html" in current_url, f"Login failed, landed on: {current_url}"
    print("PASS: Login successful, redirected to:", current_url)
    driver.save_screenshot("assignment1.png")
    
finally:
    driver.quit()
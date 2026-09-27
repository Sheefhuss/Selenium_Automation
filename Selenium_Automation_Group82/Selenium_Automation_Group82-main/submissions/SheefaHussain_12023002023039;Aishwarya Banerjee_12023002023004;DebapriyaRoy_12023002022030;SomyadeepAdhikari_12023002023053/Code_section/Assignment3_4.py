from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/login"
driver.get(url)

print(f"Navigated to: {url}")
print("-" * 30)

#ASSIGNMENT 3: CSS Selector Challenge (Wildcards)

print("Executing Assignment 3: Wildcard CSS Selectors...")

username_field = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")
username_field.send_keys("Sheefa")
print("Found the Username field using [id^='user'] and typed the username.")

password_field = driver.find_element(By.CSS_SELECTOR, "input[id*='pass']")
password_field.send_keys("SuperSecretPassword!")
print("Found the Password field using [id*='pass'] and typed the password.")

print("-" * 30)

# ASSIGNMENT 4: Child Nodes Using CSS

print("Executing Assignment 4: Child Node CSS Selectors...")

# Locate the Login button nested inside the form using a descendant selector
# The form has id="login", and the button is a child inside it.
nested_button = driver.find_element(By.CSS_SELECTOR, "form label")
nested_button.click()

#direct_child_button = driver.find_element(By.CSS_SELECTOR, "button > i")
#direct_child_button.click()
print("Clicked the Login button using the 'form button' child selector.")

print("-" * 30)

time.sleep(3)

print("Test finished successfully! Browser closed.")
driver.quit()
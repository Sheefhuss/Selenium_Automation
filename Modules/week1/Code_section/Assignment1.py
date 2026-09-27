from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open the login webpage
driver.get("https://the-internet.herokuapp.com/login")

# 1. Locate Username using ID
username = driver.find_element(By.ID, "username")
print("Username field found:", username)

# 2. Locate Password using NAME
password = driver.find_element(By.NAME, "password")
print("Password field found:", password)

# 3. Locate an input element using TAG_NAME
input_element = driver.find_element(By.TAG_NAME, "input")
print("Input element found:", input_element)

# 4. Locate Elemental Selenium link using LINK_TEXT
link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
print("Link text:", link.text)

# 5. Locate Login button using CLASS_NAME
login_button = driver.find_element(By.CLASS_NAME, "radius")
print("Login button text:", login_button.text)

# Close the browser
driver.quit()

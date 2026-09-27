import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

with open("modules/module2/login_data.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:

        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys(row["username"])
        driver.find_element(By.ID, "password").send_keys(row["password"])
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        driver.save_screenshot(
            "Assignment_8_row_" + row["username"] + "_" + row["expected"] + ".png"
        )

        if row["expected"] == "success":
            assert "/secure" in driver.current_url
            print(row["username"], "LOGIN SUCCESS")

        else:
            assert "/login" in driver.current_url
            print(row["username"], "LOGIN FAILED - VALIDATION CORRECT")

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    table = driver.find_element(By.XPATH, "//table[@name='courses']")
    driver.execute_script("arguments[0].scrollIntoView(true);", table)

    time.sleep(5)

    target_course = "Master Selenium Automation in simple Python Language"

    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")

        if cols:
            course_name = cols[1].text.strip()
            price = cols[2].text.strip()

            if course_name == target_course:
                print(f"Matched Course: '{course_name}'")
                print(f"Extracted Price: {price}")
                break

    driver.save_screenshot("assignment5_web_tables.png")

finally:
    driver.quit()
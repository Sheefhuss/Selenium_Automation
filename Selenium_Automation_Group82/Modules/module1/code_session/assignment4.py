from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # 1. Accept JS Alert
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print("Alert text:", alert.text)
    alert.accept()

    # 2. Dismiss JS Confirm Box
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    confirm = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print("Confirm text:", confirm.text)
    confirm.dismiss()

    # 3. Input Text into JS Prompt Box & Accept
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    prompt = WebDriverWait(driver, 5).until(EC.alert_is_present())
    prompt.send_keys("Selenium Automation")
    prompt.accept()

    # Save screenshot
    driver.save_screenshot("assignment4_screenshot_js_alerts.png")

finally:
    driver.quit()
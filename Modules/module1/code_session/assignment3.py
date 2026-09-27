from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # --- Part A: Checkboxes ---
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    for i, box in enumerate(checkboxes):
        if not box.is_selected():
            box.click()
        print(f"Checkbox {i + 1} selected state: {box.is_selected()}")
    driver.save_screenshot("screenshot_checkbox.png")
    # --- Part B: Autocomplete dropdown ---
    driver.get("https://jqueryui.com/resources/demos/autocomplete/default.html")

    wait = WebDriverWait(driver, 10)

    # Directly wait for the search box to be present
    search_box = wait.until(EC.presence_of_element_located((By.ID, "tags")))
    search_box.send_keys("Ja") 

    # Wait for suggestions list to appear
    suggestions = wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.ui-autocomplete li"))
    )

    target = "Java"
    for suggestion in suggestions:
        if suggestion.text.strip() == target:
            suggestion.click()
            print(f"Selected suggestion: {target}")
            break

    driver.save_screenshot("assignment3.png")

finally:
    driver.quit()
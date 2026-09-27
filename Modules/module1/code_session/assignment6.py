from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def show_and_accept_alert(driver, message):
    """Triggers an alert safely, pauses so you can read it, then accepts it."""
    driver.execute_script("alert(arguments[0]);", message)
    time.sleep(1) 
    driver.switch_to.alert.accept()
    time.sleep(1)

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    main_window_handle = driver.current_window_handle
    
    show_and_accept_alert(driver, "TASK 1 START: Main page loaded. Next, scrolling down to the Iframe.")

    # HANDLE IFRAME
    iframe_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "courses-iframe"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", iframe_element)
    time.sleep(3)
    driver.switch_to.frame(iframe_element)
    
    show_and_accept_alert(driver, "INSIDE IFRAME: Driver focus is now inside the embedded frame!")
    driver.switch_to.default_content()
    
    show_and_accept_alert(driver, "BACK TO MAIN PAGE: Exited iframe. Scroll back to top for tab test.")
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    show_and_accept_alert(driver, "TASK 2 START: Clicking the 'Open Tab' button now.")
    driver.find_element(By.ID, "opentab").click()

    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
    all_handles = driver.window_handles

    for handle in all_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            break
    time.sleep(3)

    new_tab_title = driver.title
    show_and_accept_alert(driver, f"NEW TAB DETECTED! Context switched. Title: '{new_tab_title}'")
    time.sleep(3)
    
    # Take screenshot
    driver.save_screenshot("assignment6_screenshot_windows_iframes.png")
    
    driver.close()

    # RETURN TO ORIGINAL TAB
    driver.switch_to.window(main_window_handle)
    show_and_accept_alert(driver, "EXPERIMENT 6 COMPLETE: Successfully returned to original main layout!")

finally:
    driver.quit()
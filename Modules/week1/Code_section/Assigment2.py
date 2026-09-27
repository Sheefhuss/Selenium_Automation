from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")

links = driver.find_elements(By.TAG_NAME, "a")

print(f"Total links found on the page: {len(links)}")
print("-" * 30)

for link in links:
    link_text = link.text
    if link_text.strip(): 
        print(link_text)

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(16)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
content = driver.find_element(By.CSS_SELECTOR, "#content")
print(content.find_element(By.CSS_SELECTOR, "p.bg-success").text)

driver.quit()

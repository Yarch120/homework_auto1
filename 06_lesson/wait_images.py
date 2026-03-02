from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(40)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

driver.find_element(By.CSS_SELECTOR, "#landscape")
aw = (driver.find_element(By.CSS_SELECTOR, "#award"))
src_value = aw.get_attribute("src")
print(src_value)
driver.quit()

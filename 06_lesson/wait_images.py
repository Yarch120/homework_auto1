from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


wait = WebDriverWait(driver, timeout=20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))

aw = (driver.find_element(By.CSS_SELECTOR, "#award"))
src_value = aw.get_attribute("src")
print(src_value)
driver.quit()

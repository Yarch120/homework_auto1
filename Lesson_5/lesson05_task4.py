from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_input = driver.find_element(By.CSS_SELECTOR, "#username")
search_input.send_keys("tomsmith")
search_input = driver.find_element(By.CSS_SELECTOR, "#password")
search_input.send_keys("SuperSecretPassword!")
check_inputt = driver.find_element(By.CSS_SELECTOR, ".radius")
check_inputt.click()
answer = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(answer)
driver.quit()
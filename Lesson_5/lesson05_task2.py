from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
search_field = ".btn-primary"
check_inputt = driver.find_element(By.CSS_SELECTOR, search_field)
check_inputt.click()
sleep(2)
check_inputt.click()
sleep(2)
check_inputt.click()
sleep(2)
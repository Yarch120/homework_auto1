from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")
search_input = driver.find_element(By.TAG_NAME, "input")
driver.execute_script("arguments[0].type = 'text';", search_input)
search_input.send_keys("Sky")
sleep(1) #убедиться в вводе данных 
search_input.clear()
search_input.send_keys("Pro")
sleep(1) #убедиться в вводе данных 
search_input.clear()
driver.quit()
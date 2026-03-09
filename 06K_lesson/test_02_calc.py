import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium. webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout=50)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    result_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    answ = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert answ == "15"

    driver.quit()
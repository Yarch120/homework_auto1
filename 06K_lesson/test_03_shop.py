import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium. webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, timeout=20)

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "[class=shopping_cart_link]").click()

    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ярослав")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Чекашкин")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("117036")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    Total = driver.find_element(By.CSS_SELECTOR, "[class=summary_total_label]").text
    total_value = Total.replace("Total: $", "").strip()

    driver.quit()

    assert total_value == "58.29", f"Ожидалась сумма $58.29, получена {Total}"
    print(f"Итоговая сумма корректна: {Total}")

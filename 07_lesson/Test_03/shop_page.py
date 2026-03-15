from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def authorization(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def waiting(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class=shopping_cart_link]").click()

    def go_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def personal_inform(self):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ярослав")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Чекашкин")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("117036")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def check_form_submission(self):
        Total = self.driver.find_element(By.CSS_SELECTOR, "[class=summary_total_label]").text
        total_value = Total.replace("Total: $", "").strip()
        assert total_value == "58.29", f"Ожидалась сумма $58.29, получена {Total}"
        print(f"Итоговая сумма корректна: {Total}")

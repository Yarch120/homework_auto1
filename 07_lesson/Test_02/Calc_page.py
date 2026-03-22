from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self._own_driver = True
        else:
            self.driver = driver
            self._own_driver = False
        self.wait = WebDriverWait(self.driver, 50)

    def open (self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
    
    def clear_form (self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    def waiting (self, numb):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(numb)

    def example (self,):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    def check_form_submission(self):
        answ = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert answ == "15"

    def close(self):
        if self._own_driver:
            self.driver.quit()

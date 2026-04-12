"""
Модуль содержит класс ShopPage для работы со страницей интернет-магазина.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Тестирование интернет-магазина")
@allure.story("Покупка товаров и проверка итоговой суммы")
class ShopPage:
    """
    Класс для работы со страницей интернет-магазина.
    Содержит методы для авторизации, добавления товаров в корзину,
    оформления заказа и проверки итоговой суммы.
    """
    def __init__(self, driver=None):
        """Инициализация страницы магазина"""
        if driver is None:
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self._own_driver = True
        else:
            self.driver = driver
            self._own_driver = False
        self.wait = WebDriverWait(self.driver, 10)
    
    @allure.step("Открытие страницы магазина")
    def open(self):
        """Открывает страницу интернет-магазина"""
        self.driver.get("https://www.saucedemo.com")

    @allure.step("Ожидание загрузки страницы")
    def waiting(self):
        """Ожидает полной загрузки страницы (readyState = complete)"""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    
    @allure.step("Авторизация в магазине")
    def authorization(self):
        """Выполняет авторизацию с тестовыми учётными данными, используя локаторы"""
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self):
        """Добавляет три товара в корзину и переходит к её просмотру"""
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class=shopping_cart_link]").click()

    @allure.step("Переход к оформлению заказа")
    def go_cart(self):
        """Нажимает кнопку Checkout для перехода к оформлению заказа"""
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    @allure.step("Заполнение персональных данных")
    def personal_inform(self):
        """Заполняет форму с персональными данными и продолжает оформление"""
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ярослав")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Чекашкин")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("117036")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Проверка итоговой суммы заказа")
    def check_form_submission(self):
        """Проверяет, что итоговая сумма заказа равна $58.29"""
        Total = self.driver.find_element(By.CSS_SELECTOR, "[class=summary_total_label]").text
        total_value = Total.replace("Total: $", "").strip()
        assert total_value == "58.29", f"Ожидалась сумма $58.29, получена {Total}"
        print(f"Итоговая сумма корректна: {Total}")

    @allure.step("Закрытие браузера")
    def close(self):
        """Окончание ссесии"""
        if self._own_driver:
            self.driver.quit()

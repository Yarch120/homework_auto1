"""
Модуль содержит класс CalcPage для работы со страницей медленного калькулятора.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("Тестирование веб-приложений")
@allure.feature("Страница калькулятора")
@allure.story("Проверка работы калькулятора с задержкой")
class CalcPage:
    """
    Класс для работы со страницей медленного калькулятора.
    Содержит методы для настройки задержки, выполнения вычислений и проверки результата.
    """
    def __init__(self, driver=None):
        """
        Инициализация страницы калькулятора.
        """
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self._own_driver = True
        else:
            self.driver = driver
            self._own_driver = False
        self.wait = WebDriverWait(self.driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open (self):
        """Открывает страницу с медленным калькулятором"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
    
    @allure.step("Очистка поля задержки")
    def clear_form (self):
        """Очищает поле ввода задержки"""
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    @allure.step("Установка задержки: {numb} секунд")
    def waiting (self, numb: str):
        """Устанавливает значение задержки в поле ввода"""
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(numb)

    @allure.step("Выполнение вычисления 7 + 8")
    def example (self):
        """Выполняет арифметическую операцию 7 + 8 на калькуляторе. Ожидает появления результата 15 на экране"""
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step("Проверка результата вычисления")
    def check_form_submission(self):
        """Проверяет, что результат вычисления равен 15"""
        answ = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert answ == "15"

    @allure.step("Закрытие браузера")
    def close(self):
        """Окончание ссесии"""
        if self._own_driver:
            self.driver.quit()

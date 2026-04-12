"""
Модуль содержит класс FormPage для работы со страницей формы данных.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("Тестирование веб-форм")
@allure.story("Заполнение и валидация полей формы")
class FormPage:

    """Класс для работы со страницей формы данных. Содержит методы для заполнения полей, отправки формы и проверки валидации."""
    @allure.step("Открытие браузера, пресейв для заполнения форм")
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self._own_driver = True
        else:
            self.driver = driver
            self._own_driver = False
        self.wait = WebDriverWait(self.driver, 10)
        # Тестовые данные для заполнения формы
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("переход на страницу")
    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    @allure.step("Заполнение полей формы")
    def fill_form(self):
        """Заполняет все поля формы тестовыми данными из словаря fields."""
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Отправка формы")
    def submit_form(self):
        """Нажимает кнопку отправки формы."""
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Получение CSS-класса поля")
    def get_field_class(self, field_id):
        """
        Возвращает CSS-класс указанного поля.
        Returns:
            str: CSS-класс элемента
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверка подсветки поля Zip Code как ошибочного")
    def check_zip_code_error(self):
        """
        Проверяет, что поле Zip Code имеет класс alert-danger.
        Returns:
            bool: True если поле подсвечено как ошибочное, иначе False
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка правильности заполнения остальных полей")
    def check_fields_success(self):
        """
        Проверяет, что все поля (кроме Zip Code) имеют класс success.
        Returns:
            bool: True если все поля успешны, иначе False
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка соответствия полей")
    def check_form_submission(self):
        """
        Выполняет комплексную проверку формы:
        - Zip Code должен быть ошибочным
        - Остальные поля должны быть успешными
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()

    @allure.step("Закрытие браузера и выход")
    def close(self):
        """Окончание ссесии"""
        if self._own_driver:
            self.driver.quit()

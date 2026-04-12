"""
Модуль содержит тесты для проверки формы данных.
"""
import pytest
from Form_page import FormPage
import allure


@allure.suite("Веб-форма")
@allure.epic("Тестирование веб-форм")
@allure.feature("Форма данных")
@allure.title("Проверка валидации формы с пустым полем Zip Code")
@allure.description("""
    Тест проверяет корректность валидации формы:
    1. Заполняются все поля формы
    2. Поле Zip Code оставляется пустым
    3. После отправки формы поле Zip Code должно подсвечиваться красным (alert-danger)
    4. Остальные поля должны подсвечиваться зелёным (success)
    """)
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow():
    form_page = FormPage()
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()
    form_page.close()

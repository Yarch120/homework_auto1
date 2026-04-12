"""
Модуль содержит тесты для проверки работы медленного калькулятора.
"""
import pytest
from Calc_page import CalcPage
import allure


@allure.suite("Медленный калькулятор")
@allure.epic("Тестирование веб-приложений")
@allure.feature("Медленный калькулятор")
@allure.title("Проверка сложения 7 + 8 с задержкой 45 секунд")
@allure.description("""
    Тест проверяет работу калькулятора с искусственной задержкой:
    1. Устанавливается задержка 45 секунд
    2. Выполняется операция 7 + 8
    3. Ожидается результат 15
    """)
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow():
    calc_page = CalcPage()
    calc_page.open()
    calc_page.clear_form()
    calc_page.waiting(45)  #ввести значение сколько секунд будет обрабатываться запрос
    calc_page.example()
    calc_page.check_form_submission()
    calc_page.close()

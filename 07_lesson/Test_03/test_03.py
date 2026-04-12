"""
Модуль содержит тесты для проверки интернет-магазина.
"""
import pytest
from shop_page import ShopPage
import allure


@allure.suite("Интернет-магазин")
@allure.epic("Тестирование интернет-магазина")
@allure.feature("Корзина и оформление заказа")
@allure.title("Проверка итоговой суммы заказа из трёх товаров")
@allure.description("""
    Тест проверяет корректность расчёта итоговой суммы заказа:
    1. Авторизация в магазине
    2. Добавление трёх товаров в корзину
    3. Оформление заказа с заполнением персональных данных
    4. Проверка итоговой суммы (ожидается $58.29)
    """)
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow():
    shop_page = ShopPage()

    shop_page.open()
    shop_page.waiting()
    shop_page.authorization()
    shop_page.waiting()
    shop_page.add_to_cart()
    shop_page.waiting()
    shop_page.go_cart()
    shop_page.waiting()
    shop_page.personal_inform()
    shop_page.waiting()
    shop_page.check_form_submission()
    shop_page.close()

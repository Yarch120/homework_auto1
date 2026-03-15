import pytest
from selenium import webdriver
from shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    shop_page = ShopPage(driver)
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

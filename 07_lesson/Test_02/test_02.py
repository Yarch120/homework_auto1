import pytest
from selenium import webdriver
from Calc_page import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.clear_form()
    calc_page.waiting(45)  #ввести значение сколько секунд будет обрабатываться запрос
    calc_page.example()
    calc_page.check_form_submission()

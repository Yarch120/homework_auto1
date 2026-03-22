import pytest
from Calc_page import CalcPage

def test_form_submission_flow():
    calc_page = CalcPage()
    calc_page.open()
    calc_page.clear_form()
    calc_page.waiting(45)  #ввести значение сколько секунд будет обрабатываться запрос
    calc_page.example()
    calc_page.check_form_submission()
    calc_page.close()

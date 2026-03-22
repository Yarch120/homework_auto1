import pytest
from shop_page import ShopPage

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

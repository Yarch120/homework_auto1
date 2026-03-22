import pytest
from Form_page import FormPage

def test_form_submission_flow():
    form_page = FormPage()
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()
    form_page.close()

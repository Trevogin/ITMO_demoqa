import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys

def test_login_form_validate(browser):
    form_page=FormPage(browser)
    form_page.visit()

    assert form_page.first_name.get_dom_attribute('placeholder') == "First Name"
    assert form_page.last_name.get_dom_attribute('placeholder') == "Last Name"
    assert form_page.email.get_dom_attribute('placeholder') == "name@example.com" and form_page.email.get_dom_attribute('pattern')=='^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    form_page.btn_submit.click_force()
    assert form_page.user_form.get_dom_attribute('class')=='was-validated'


def test_state(browser):
    form_page=FormPage(browser)
    form_page.visit()

    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)

def test_state_2(browser):
    form_page=FormPage(browser)
    form_page.visit()

    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.inp_state.send_keys('NCR')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)

def test_state_3(browser):
    form_page=FormPage(browser)
    form_page.visit()

    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.btn_state.click()
    form_page.inp_state.send_keys(Keys.PAGE_DOWN)
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)
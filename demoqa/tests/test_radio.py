import time
import pytest
from pages.radio import Radio

@pytest.mark.skipif(True,reason='просто пропуск')
def test_decor(browser):
    radio=Radio(browser)
    radio.visit()

    radio.yes.click_force()
    time.sleep(2)
    assert radio.text.get_text()=="You have selected Yes"

    radio.impressive.click_force()
    time.sleep(2)
    assert radio.text.get_text()=='You have selected Impressive'

    assert 'disabled' in radio.no.get_dom_attribute('class')
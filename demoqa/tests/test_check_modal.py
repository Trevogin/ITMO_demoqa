import time

import pytest
from pages.modal_dialogs import ModalDialogsPage

def test_check_modal(browser):
    modal_page = ModalDialogsPage(browser)
    modal_page.visit()

    # Малое модальное окно
    modal_page.btn_small_modal.click()
    time.sleep(2)
    small_modal_text = modal_page.modal_small.get_text()
    assert "Small Modal" in small_modal_text, "Малое модальное окно не появилось или текст не совпадает"
    modal_page.btn_close_small.click()
    time.sleep(2)


    # Большое модальное окно
    modal_page.btn_large_modal.click()
    time.sleep(2)
    large_modal_text = modal_page.modal_large.get_text()
    assert "Large Modal" in large_modal_text, "Большое модальное окно не появилось или текст не совпадает"
    modal_page.btn_close_large.click()
    time.sleep(2)
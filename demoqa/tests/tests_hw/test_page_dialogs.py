from pages.modal_dialogs import ModalDialogsPage

def test_modal_elements(browser):
    modal_dialogs_page=ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.btn_modal.check_count_elements(count=2) # count=5 не работает

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    browser.refresh()
    modal_dialogs_page.icon.click()

    browser.back()
    browser.set_window_size(900,400)
    browser.forward()
    assert browser.current_url=='https://demoqa.com/'
    assert browser.title=='DEMOQA'
    browser.set_window_size(1000, 1000)
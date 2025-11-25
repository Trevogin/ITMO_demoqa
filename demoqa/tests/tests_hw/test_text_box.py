from pages.text_box import TextBox

def test_text_box(browser):
    text_box_page=TextBox(browser)
    text_box_page.visit()

    text_box_page.name.send_keys('test_name')
    text_box_page.currentAddress.send_keys('test_address')
    text_box_page.btn_submit.click_force()

    assert not text_box_page.name.get_dom_attribute('Full Name') == 'test_name'
    assert not text_box_page.name.get_dom_attribute('Current Address') == 'test_address'
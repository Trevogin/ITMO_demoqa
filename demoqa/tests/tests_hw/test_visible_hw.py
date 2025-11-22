from pages.accordian import Accordian
import time

def test_visible_accordion(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()

    assert accordian_page.section1_content_p.find_element().is_displayed()
    accordian_page.section1_heading.click()
    time.sleep(2)
    assert not accordian_page.section1_content_p.find_element().is_displayed()

def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()

    assert not accordian_page.section2_content_p1.find_element().is_displayed()
    assert not accordian_page.section2_content_p2.find_element().is_displayed()
    assert not accordian_page.section3_content_p.find_element().is_displayed()
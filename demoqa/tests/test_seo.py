import time
from pages.demoqa import DemoQa
from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
import pytest


def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('pages', [Accordian, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
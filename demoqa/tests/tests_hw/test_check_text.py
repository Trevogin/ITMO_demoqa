from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def get_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.check_text()

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    demo_qa_page.text_elements()

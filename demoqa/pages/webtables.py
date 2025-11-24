from pages.base_page import BasePage
from components.components import WebElement


class Webtables(BasePage):

    def __init__(self,driver):
        self.base_url='https://demoqa.com/webtables'
        super().__init__(driver,self.base_url)

        self.btn_delete_row = WebElement(driver, '[id^="delete-record-"]')
        self.no_data = WebElement(driver, 'div.rt-noData')

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')

        self.firstname = WebElement(driver, '#firstName')
        self.lastname = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_edit_row = WebElement(driver, '[id^="edit-record-"]')
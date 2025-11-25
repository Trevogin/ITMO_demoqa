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

        self.rows = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.btn_prev = WebElement(driver,'//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/button','xpath')
        self.btn_next = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.total_pages = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')
        self.newstr = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div')
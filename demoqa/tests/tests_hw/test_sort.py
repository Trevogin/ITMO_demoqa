from selenium.webdriver.common.by import By
from pages.webtables import Webtables

def test_columns_sorting(browser):
    webtables_page = Webtables(browser)
    webtables_page.visit()

    # Находим все заголовки столбцов таблицы
    headers = browser.find_elements(By.CSS_SELECTOR, "div.rt-resizable-header-content")
    assert headers, "Заголовки столбцов не найдены!"

    for header in headers:
        header.click()

        # Получаем родителя — .rt-resizable-header т.к именно в нем меняется класс при нажатии и попытке сортировки
        parent = header.find_element(By.XPATH, "./..")
        class_value = parent.get_dom_attribute('class')
        # Проверяем, что в классе появился признак сортировки
        assert ("-sort-asc" in class_value) or ("-sort-desc" in class_value), (
            f"Заголовок '{header.text}' не отсортирован после клика: {class_value}"
        )
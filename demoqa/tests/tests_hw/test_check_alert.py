from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.alerts import Alerts

def test_check_alert(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()

    alerts_page.btn_timer_alert.click()

    # Ждём появления alert (не более 7 секунд)
    alert = WebDriverWait(browser, 7).until(EC.alert_is_present())

    # Проверяем, что текст алерта не пустой
    assert alert.text != '', "Текст алерта пустой"

    alert.accept()
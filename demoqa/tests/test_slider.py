import time
from pages.slider import Slider
from selenium.webdriver.common.keys import Keys

def test_slider(browser):
    slider=Slider(browser)
    slider.visit()
    
    assert slider.slider.exist()
    assert slider.inp.exist()

    slider.inp.send_keys('50') #меняем через инпут (окошко правее слайдера)
    time.sleep(2)
    slider.inp.send_keys('25')#возвращаем обратно
    while not slider.inp.get_dom_attribute('value')=='50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)
    assert slider.slider.get_dom_attribute('value')=='50'
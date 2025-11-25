import pytest
from pages.demoqa import DemoQa

@pytest.mark.skip
def test_decor(browser):
    demoqa=DemoQa(browser)
    demoqa.visit()

    assert demoqa.h5.check_count_elements(6)
    for element in demoqa.h5.find_elements():
        assert element.text != ''

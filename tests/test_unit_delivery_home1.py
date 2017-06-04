from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos

#Unit Test for Delivery on Home Page
@pytest.mark.usefixtures('driver')
class TestDeliverHome(object):
    def test_link(self,driver):
        navigate_to_dominos(driver)
        button_text=Keywords.getText(driver, "//*[contains(@class,'js-delivery')][contains(text(),'Delivery')]")
        assert (button_text=='DELIVERY'),"Text of Delivery Button is incorrect, expected: %s"%'DELIVERY'
        Keywords.ClickElement(driver, button_text)
        assert (driver.title=="Location Search - Location Search"),"After Delivery Button is clicked either page not visible or wrong page"
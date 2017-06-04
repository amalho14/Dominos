from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos
from selenium.webdriver.support.wait import WebDriverWait

#Unit Test for Delivery on Home Page
@pytest.mark.usefixtures('driver')
class TestDeliveryHome(object):
    
    def test_delivery_button(self,driver):
        navigate_to_dominos(driver)
        delivery_button="//*[contains(@class,'js-delivery')]"
        button_text=Keywords.getText(driver, delivery_button)
        assert (button_text=='DELIVERY'),"Text of Delivery Button is incorrect, expected: %s"%'DELIVERY'
        assert (Keywords.isElementEnabled(driver, deliveryButton) is True),"Deliver Button is not enabled"
        Keywords.ClickElement(driver, delivery_button)
        try:
            Keywords.isElementVisible(driver,"//*[@class='form']/div/div/h2/span")
        finally:
            assert (driver.title=="Location Search - Location Search"),"After Delivery Button is clicked either page not visible or wrong page"
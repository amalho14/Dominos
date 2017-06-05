from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos



@pytest.mark.usefixtures('driver')
class TestCarryoutSelectPizza(object):
    
    def test_carryout_pizza_selec_unit(self,driver):
        #Get to the pizza select page
        navigate_to_dominos(driver)
        carryout_button="//*[contains(@class,'js-carryout')]"
        Keywords.ClickElement(driver, carryout_button)
        city="//*[@name='City']" 
        Keywords.enterText(driver,"Tempe",city)
        state="//*[@name='Region']"
        Keywords.ClickElement(driver,state)
        state_AZ="//*[@name='Region']/option[contains(text(),'AZ')]"
        Keywords.ClickElement(driver,state_AZ)
        zip_code="//*[@name='Postal_Code']"
        Keywords.enterText(driver,"85281",zip_code)
        driver.submit()
        
from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos




@pytest.mark.usefixtures('driver')
class TestCarryoutSelectPizza(object):
    def pre_req(self,driver):
        #Get to the pizza select page
        navigate_to_dominos(driver)
        carryout_button="//*[contains(@class,'js-carryout')]"
        Keywords.ClickElement(driver, carryout_button)
        carryoutRadio="//*[@name='Service_Type'][contains(@value,'Carryout')]"
        Keywords.isElementVisible(driver,carryoutRadio)
        
        city="//*[@name='City']" 
        cityValue="TEMPE"
        Keywords.enterText(driver,cityValue,city)
        state="//*[@name='Region']"
        Keywords.ClickElement(driver,state)
        state_AZ="//*[@name='Region']/option[contains(text(),'AZ')]"
        stateValue="AZ"
        Keywords.ClickElement(driver,state_AZ)
        zip_code="//*[@name='Postal_Code']"
        zip_codeValue="85281"
        Keywords.enterText(driver,"85281",zip_code)
        submit="//*[@type='submit']"
        Keywords.ClickElement(driver,submit)
        
        orderCarryOutLocation="//*[contains(@class,'search-results-list')]/div/div[1]/div/a"
        Keywords.ClickElement(driver,orderCarryOutLocation)
    
    def test_carryout_pizza_select_unit(self,driver):
        #Get to the pizza select page
        navigate_to_dominos(driver)
        carryout_button="//*[contains(@class,'js-carryout')]"
        Keywords.ClickElement(driver, carryout_button)
        carryoutRadio="//*[@name='Service_Type'][contains(@value,'Carryout')]"
        Keywords.isElementVisible(driver,carryoutRadio)
        
        city="//*[@name='City']" 
        cityValue="TEMPE"
        Keywords.enterText(driver,cityValue,city)
        state="//*[@name='Region']"
        Keywords.ClickElement(driver,state)
        state_AZ="//*[@name='Region']/option[contains(text(),'AZ')]"
        stateValue="AZ"
        Keywords.ClickElement(driver,state_AZ)
        zip_code="//*[@name='Postal_Code']"
        zip_codeValue="85281"
        Keywords.enterText(driver,"85281",zip_code)
        submit="//*[@type='submit']"
        Keywords.ClickElement(driver,submit)
        
        Keywords.isElementVisible(driver,"//*[@class='based-on']")
        orderCarryOutLocation="//*[contains(@class,'search-results-list')]/div/div[1]/div/a"
        Keywords.ClickElement(driver,orderCarryOutLocation)
        
        awaitingOrder="//*[contains(@class,'js-emptyMessage')]"
        Keywords.isElementVisible(driver,awaitingOrder)
        myAddress="%s, %s %s",(cityValue,state_AZ,zip_code)
        myLocation="//*[contains(@class,'qa-MyLoc')]/li"
        elements=Keywords.WebElements(driver,myLocation)
        for element in elements:
            if(element.text!=""):
                assert (element.get_text()==myAddress),"Address not same for checkout"
                
        
        
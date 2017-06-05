from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures('driver')
class TestCarryoutAddress(object):
    
    def test_carryout_address_unit(self,driver):
        navigate_to_dominos(driver)
        carryout_button="//*[contains(@class,'js-carryout')]"
        Keywords.ClickElement(driver, carryout_button)
        carryoutRadio="//*[@name='Service_Type'][contains(@value,'Carryout')]"
        assert (Keywords.isElementSelected(driver, carryoutRadio) is True), "Carryout Icon is not selected"
        
        state_values=['Select', 'AK', 'AL', 'AR', 'AZ', 
              'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 
              'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 
              'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 
              'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        state="//*[@id='Region']"
        Keywords.ClickElement(driver,state)
        states=state+"/option"
        stateElements=Keywords.WebElements(driver,states)
        statesList=[]
        for state in statesElements:
            statesList.append(state.text) 
        for state in state_values:
            assert(state in statesList),"State not available in list: %s"%state
        
        city="//*[@name='City']"
        assert (Keywords.getType(driver, city)=="text"),"Attribute for city is incorrect"
        assert (Keywords.getAttributeLength(driver,city)=='40'),"Max Length for city is incorrect"
        
        zip_code="//*[@name='Postal_Code']"
        assert (Keywords.getType(driver, zip_code)=="tel"),"Attribute for Zip Code is incorrect"
        assert (Keywords.getAttributeLength(driver,zip_code)=='10'),"Max Length for Zip Code is incorrect"
        
        city="//*[@for='City']" 
        assert(Keywords.getText(driver, city)=="*City:"),"City text doesn't match"
        
        state="//*[@for='Region']"
        assert(Keywords.getText(driver, state)=="*State:"),"State doesn't match"
        
        zip_code="//*[@for='Postal_Code']"
        assert(Keywords.getText(driver, zip_code)=="*Zip Code:"),"Zip Code doesn't match"
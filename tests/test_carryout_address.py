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
        
        toggleZip="//*[contains(@class,'toggle-zip')]/a"
        if(len(driver.find_elements_by_xpath((toggleZip)))>0):
            Keywords.ClickElement(driver,toggleZip) 
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
        for state in stateElements:
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
         
         
    def test_carryout_address_api(self,driver):
        navigate_to_dominos(driver)
        carryout_button="//*[contains(@class,'js-carryout')]"
        Keywords.ClickElement(driver, carryout_button)
        submit="//*[contains(@class,'js-search-cta')]"
        Keywords.ClickElement(driver, submit)
        error="This field is required."
         
        city_error="//*[@id='City-error']"
        assert (Keywords.getText(driver, city_error)==error), "City Error is not the same as expected"
         
        state_error="//*[@id='Region-error']"
        assert (Keywords.getText(driver, state_error)==error),"State Error is not the same as expected"
         
        postal_code_error="//*[@id='Postal_Code-error']"
        assert (Keywords.getText(driver, postal_code_error)==error),"Zip Code Error is not the same as expected"
     
    def test_carryout_address_ui_component(self,driver):
        navigate_to_dominos(driver)
        carryout_button="//*[contains(@class,'js-carryout')]"
        Keywords.ClickElement(driver, carryout_button)
        
        zip_code="//*[@name='Postal_Code']"
        randomZip=Keywords.generateRandom('letter','digits','punctuation',20)
        Keywords.enterText(driver,randomZip,zip_code)
        Keywords.WebElement(driver,zip_code).send_keys(Keys.TAB)
        assert (Keywords.getAttributeValue(driver,zip_code)!=randomZip),"Zip Code entered with Alphabets and Punctuation"
        
        toggleZip="//*[contains(@class,'toggle-zip')]/a"
        if(len(driver.find_elements_by_xpath((toggleZip)))>0):
            Keywords.ClickElement(driver,toggleZip)
        
        city="//*[@name='City']" 
        randomCity=Keywords.generateRandom('letter','digits','punctuation',20)
        Keywords.enterText(driver,randomCity,city)
        Keywords.WebElement(driver,city).send_keys(Keys.TAB)
        assert (Keywords.getAttributeValue(driver,city)==randomCity),"City is not entered correctly"
         
        state="//*[@name='Region']"
        Keywords.ClickElement(driver,state)
        state_AZ="//*[@name='Region']/option[contains(text(),'AZ')]"
        Keywords.ClickElement(driver,state_AZ)
         
         
         
         
         
         
         
         
         
         
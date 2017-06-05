from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures('driver')
class TestDeliveryAddress(object):
    
    
    def test_delivery_address_unit(self,driver):
        navigate_to_dominos(driver)
        delivery_button="//*[contains(@class,'js-delivery')]"
        Keywords.ClickElement(driver, delivery_button)
        
        deliveryRadio="//*[@name='Service_Type'][contains(@value,'Delivery')]"
        assert (Keywords.isElementSelected(driver, deliveryRadio) is True), "Delivery Icon is not selected"
        
        addressPath="//*[@id='Address_Type_Select']/option[contains(text(),'House')]"
        Keywords.ClickElement(driver, addressPath)
        
        types_of_address=['Apartment','Business','Campus/Base','Hotel','Dormitory','Other']
        address="//*[@id='Address_Type_Select']/option"
        assert (Keywords.isElementVisible(driver, address) is True),"Address is not available for selection"
        addressList=Keywords.WebElements(driver, address)
        address_values=[]
        for add in addressList:
            address_values.append(add.text)
        for add in types_of_address:
            assert(add in address_values),"Address not available in list: %s"%add
        
        street_address="//*[@name='Street']"
        assert (Keywords.getType(driver, street_address)=="text"),"Attribute for address is incorrect, expected :%s for %s"%("text",'House')
        assert (Keywords.getAttributeLength(driver, street_address)=='40'),"Max Length for address is incorrect, expected:%s for %s"%('40','House')
        
        address_line2="//*[@name='Address_Line_2']"
        assert (Keywords.getType(driver, address_line2)=="text"),"Attribute for Address Line 2 is incorrect,expected: %s for %s" %("text",'House')
        assert (Keywords.getAttributeLength(driver,address_line2)=='40'),"Max Length for Address Line 2 is incorrect, expected:%s for %s" % ('40','House')
        
        city="//*[@name='City']"
        assert (Keywords.getType(driver, city)=="text"),"Attribute for city is incorrect, expected :%s for %s"%("text",'House')
        assert (Keywords.getAttributeLength(driver,city)=='40'),"Max Length for city is incorrect, expected:%s for %s" % ('40','House')
        
        zip_code="//*[@name='Postal_Code']"
        assert (Keywords.getType(driver, zip_code)=="tel"),"Attribute for Zip Code is incorrect,expected: %s for %s"%("tel",'House')
        assert (Keywords.getAttributeLength(driver,zip_code)=='10'),"Max Length for Zip Code is incorrect, expected:%s for %s" % ('10','House')
        
        Keywords.ClickElement(driver, "//*[@id='Address_Type_Select']/option")
        states="//*[@name='Region']/option"
        state_values=['Select', 'AK', 'AL', 'AR', 'AZ', 
              'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 
              'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 
              'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 
              'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        statesElements=Keywords.WebElements(driver, states)
        statesList=[]
        for state in statesElements:
            statesList.append(state.text) 
        for state in state_values:
            assert(state in statesList),"State not available in list: %s"%state
        
        address_type="//*[contains(@class,'js-otherAddress')]/div[1]/label"
        assert(Keywords.getText(driver, address_type)=="Address Type:"),"Text for Address Type doesn't match Address Type: 'House'"    
        street_address="//*[@for='Street']"
        assert(Keywords.getText(driver, street_address)=="*Street Address:"),"Street address text does't match for address type: 'House'"
        city="//*[@for='City']" 
        assert(Keywords.getText(driver, city)=="*City:"),"City text doesn't match for address type: 'House'"
        state="//*[@for='Region']"
        assert(Keywords.getText(driver, state)=="*State:"),"State doesn't match for address type: 'House'"
        zip_code="//*[@for='Postal_Code']"
        assert(Keywords.getText(driver, zip_code)=="*Zip Code:"),"Zip Code doesn't match for address type: 'House'"
        address_line2="//*[@for='Address_Line_2']"
        assert(Keywords.getText(driver, address_line2)=="Suite/Apt #"),"Suite/Apt# text doesn't match expected: %s for %s" % ("Suite/Apt #",add)
        
        
        
        
    def test_delivery_address_api(self,driver):
        navigate_to_dominos(driver)
        delivery_button="//*[contains(@class,'js-delivery')]"
        Keywords.ClickElement(driver, delivery_button)
        addressPath="//*[@id='Address_Type_Select']/option[contains(text(),'House')]"
        Keywords.ClickElement(driver, addressPath)
        submit="//*[contains(@class,'js-search-cta')]"
        Keywords.ClickElement(driver, submit)
        error="This field is required."
        
        state_error="//*[@id='Region-error']"
        assert (Keywords.getText(driver, state_error)==error),"State Error is not the same as expected: %s for %s" %(error,add)
        
        postal_code_error="//*[@id='Postal_Code-error']"
        assert (Keywords.getText(driver, postal_code_error)==error),"Zip Code Error is not the same as expected: %s for %s" %(error,add)
        
        city_error="//*[@id='City-error']"
        assert (Keywords.getText(driver, city_error)==error), "City Error is not the same as expected: %s for %s" %(error,add)
        
        street_error="//*[@id='Street-error']"
        assert (Keywords.getText(driver, street_error)==error),"Street Error is not the same as expected: %s for %s" % (error,add)
        
    def test_delivery_address_ui_component(self,driver):
        navigate_to_dominos(driver)
        delivery_button="//*[contains(@class,'js-delivery')]"
        Keywords.ClickElement(driver, delivery_button)
        addressPath="//*[@id='Address_Type_Select']/option[contains(text(),'House')]"
        Keywords.ClickElement(driver, addressPath)
        
        street_address="//*[@name='Street']"
        randomStreet=Keywords.generateRandom('letter','digits','punctuation',20)
        Keywords.enterText(driver,randomStreet,street_address)
        Keywords.WebElement(driver,street_address).send_keys(Keys.TAB)
        print Keywords.getAttributeValue(driver,street_address)
        #assert (Keywords.getText(driver,street_address)==randomStreet),"Street address not entered correctly %s %s" %(randomStreet,Keywords.getText(driver,street_address))
        
        address_line2="//*[@name='Address_Line_2']"
        randomAddressLine2=Keywords.generateRandom('letter','digits','punctuation',10)
        Keywords.enterText(driver,randomAddressLine2,address_line2)
        
        #assert (Keywords.getText(driver,address_line2)==randomAddressLine2),"Street address 2 not entered correctly"
        
        city="//*[@name='City']" 
        randomCity=Keywords.generateRandom('letter','digits','punctuation',20)
        Keywords.enterText(driver,randomCity,city)
        #assert (Keywords.getText(driver,city)==randomCity),"City is not entered correctly"

        state="//*[@name='Region']"
        Keywords.ClickElement(driver,state)
        state_AZ="//*[@name='Region']/option[contains(text(),'AZ')]"
        Keywords.ClickElement(driver,state_AZ)
        
        
        zip_code="//*[@name='Postal_Code']"
        randomZip=Keywords.generateRandom('letter','digits','punctuation',20)
        Keywords.enterText(driver,randomZip,zip_code)
        #assert (Keywords.getText(driver,zip_code)!=randomZip),"Zip Code entered with Alphabets and Punctuation"
        
        
        
        
        
        
        
        
        
from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos



def navigate_to_select_pizza(driver):
        #Get to the pizza select page
        navigate_to_dominos(driver)
        carryout_button="//*[contains(@class,'js-carryout')]"
        Keywords.ClickElement(driver, carryout_button)
        carryoutRadio="//*[@name='Service_Type'][contains(@value,'Carryout')]"
        Keywords.isElementVisible(driver,carryoutRadio)
        
        zip_code="//*[@name='Postal_Code']"
        zip_codeValue="85281"
        Keywords.enterText(driver,"85281",zip_code)
        toggleZip="//*[contains(@class,'toggle-zip')]/a"
        if(len(driver.find_elements_by_xpath((toggleZip)))>0):
            driver.find_element_by_xpath(toggleZip).click()
        city="//*[@name='City']" 
        cityValue="TEMPE"
        Keywords.enterText(driver,cityValue,city)
        state="//*[@name='Region']"
        Keywords.ClickElement(driver,state)
        state_AZ="//*[@name='Region']/option[contains(text(),'AZ')]"
        stateValue="AZ"
        Keywords.ClickElement(driver,state_AZ)
        
        submit="//*[@type='submit']"
        Keywords.ClickElement(driver,submit)
        Keywords.isElementVisible(driver,"//*[@class='based-on']")
        orderCarryOutLocation="//*[contains(@class,'search-results-list')]/div/div[1]/div/a"
        Keywords.ClickElement(driver,orderCarryOutLocation)
        changeOrderTimingOverlay="//*[@id='changeOrderTimingOverlay']/div/form//div/select"
        
        if(len(driver.find_elements_by_xpath(changeOrderTimingOverlay))>0):
            Keywords.ClickElement(changeOrderTimingOverlay)
            selectTime=changeOrderTimingOverlay+"/option[3]"
            Keywords.ClickElement(selectTime)
        awaitingOrder="//*[contains(@class,'js-emptyMessage')]"
        Keywords.isElementVisible(driver,awaitingOrder)

@pytest.mark.usefixtures('driver')
class TestCarryoutSelectPizza(object):
    
    #Verify if the user is able to view details while selecting pizza for pickup
    def test_carryout_pizza_select_unit(self,driver):
        #Get to the pizza select page
        navigate_to_select_pizza(driver)
        cityValue="TEMPE"
        state_AZ="AZ"
        zip_code="85281"
        
        myAddress=cityValue+', '+state_AZ+' ' +zip_code
        myLocation="//*[contains(@class,'qa-MyLoc')]/li"
        elements=Keywords.WebElements(driver,myLocation)
        for element in elements:
            if(element.text!=""):
                assert (element.text in myAddress),"Address not same for checkout"
        
        carryOutRadio="//*[@id='Service_Method_Carryout']"
        assert (Keywords.isElementSelected(driver,carryOutRadio)==True),"Carryout Radio Button is not selected while ordering"
        orderTimingNow="//*[@id='Order_Timing_Now']"
        orderTimeFuture="//*[@id='Order_Timing_Future']"
        assert(Keywords.isElementVisible(driver,orderTimingNow)==True),"Order Timing now is not visible while ordering"
        assert(Keywords.isElementVisible(driver,orderTimeFuture)==True),"Order Timing future is not visible while ordering"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        
        
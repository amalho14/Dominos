from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos


def navigate_to_select_pizza(driver):
        #Get to the pizza select page
        navigate_to_dominos(driver)
        delivery_button="//*[contains(@class,'js-delivery')]"
        Keywords.ClickElement(driver, delivery_button)
        deliveryRadio="//*[@name='Service_Type'][contains(@value,'Delivery')]"
        Keywords.isElementVisible(driver,deliveryRadio)
        
        zip_code="//*[@name='Postal_Code']"
        zip_codeValue="85281"
        Keywords.enterText(driver,"85281",zip_code)
#         toggleZip="//*[contains(@class,'toggle-zip')]/a"
#         if(len(driver.find_elements_by_xpath((toggleZip)))>0):
#             driver.find_element_by_xpath(toggleZip).click()
        city="//*[@name='City']" 
        cityValue="TEMPE"
        Keywords.enterText(driver,cityValue,city)
        state="//*[@name='Region']"
        Keywords.ClickElement(driver,state)
        state_AZ="//*[@name='Region']/option[contains(text(),'AZ')]"
        stateValue="AZ"
        Keywords.ClickElement(driver,state_AZ)
        addressPath="//*[@id='Address_Type_Select']/option[contains(text(),'House')]"
        Keywords.ClickElement(driver, addressPath)
        street_address="//*[@name='Street']"
        randomStreet="1215 E Vista Del Cerro Drive"
        Keywords.enterText(driver,randomStreet,street_address)
        address_line2="//*[@name='Address_Line_2']"
        randomAddressLine2="Apartment 1016S"
        Keywords.enterText(driver,randomAddressLine2,address_line2)
        
        submit="//*[@type='submit']"
        Keywords.ClickElement(driver,submit)
        if(len(driver.find_elements_by_xpath("//*[@class='based-on']"))>0):
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
class TestDeliverySelectPizza(object):
    
    
    def test_delivery_pizza_select_unit(self,driver):
        #Get to the pizza select page
        navigate_to_select_pizza(driver)
        myAddress="1215 E VISTA DEL CERRO DR APT 1016S"
        
        myLocation="//*[contains(@class,'qa-MyLoc')]/li[2]"
        assert (Keywords.getText(driver,myLocation) in myAddress),"Address not same for checkout"
        
        deliveryRadioButton="//*[@id='Service_Method_Delivery']"
        assert (Keywords.isElementSelected(driver,deliveryRadioButton)==True),"Carryout Radio Button is not selected while ordering"
        orderTimingNow="//*[@id='Order_Timing_Now']"
        orderTimeFuture="//*[@id='Order_Timing_Future']"
        assert(Keywords.isElementVisible(driver,orderTimingNow)==True),"Order Timing now is not visible while ordering"
        assert(Keywords.isElementVisible(driver,orderTimeFuture)==True),"Order Timing future is not visible while ordering"
        
        
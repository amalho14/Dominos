from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos
from tests.test_delivery_pizza_select import navigate_to_select_pizza
from tests.test_delivery_payment import navigate_to_payment
from selenium.webdriver.common.keys import Keys

def fill_form(driver):
    firstName="//*[@id='First_Name']"
    fName="Anvesh"
    Keywords.enterText(driver,fName,firstName)
    #assert (Keywords.getAttributeValue(driver,firstName)==fName),"First Name Not entered correctly"
    
    lastName="//*[@id='Last_Name']"
    lName="Malhotra"
    Keywords.enterText(driver,lName,lastName)
    Keywords.WebElement(driver,lastName).send_keys(Keys.TAB)
    #assert (Keywords.getAttributeValue(driver,lastName)==lName),"Last Name not entered correctly"
    
    email="//*[@id='Email']"
    emailAddress="test@xyz.com"
    Keywords.enterText(driver,emailAddress,email)
    Keywords.WebElement(driver,email).send_keys(Keys.TAB)
    #assert (Keywords.getAttributeValue(driver,email)==emailAddress),"Email Addres not entered correctly"
    
    
    callbackPhone="//*[@id='Callback_Phone']"
    phone="1234567890"
    Keywords.enterText(driver,phone,callbackPhone)
    Keywords.WebElement(driver,callbackPhone).send_keys(Keys.TAB)
    #assert (Keywords.getAttributeValue(driver,callbackPhone)==phone),"Phone not entered correctly"
    
    payAtStore="//*[contains(@class,'c-order-payment-cash')]"
    Keywords.ClickElement(driver,payAtStore)
    assert (Keywords.isElementSelected(driver,payAtStore)==True),"payment not selected correctly"
    
    #placeOrder="//*[contains(@class,'submitButton')]"
    #Keywords.ClickElement(driver,placeOrder)

@pytest.mark.usefixtures('driver')
class TestPayment(object):
    def test_e2e_delivery_dominos(self,driver):
        navigate_to_payment(driver)
        
        deliveryInstructions="//*[@id='Delivery_Instructions']"
        instruction="Call"
        Keywords.enterText(driver,instruction,deliveryInstructions)
        Keywords.WebElement(driver,deliveryInstructions).send_keys(Keys.TAB)
        #assert (Keywords.getAttributeValue(driver,deliveryInstructions)==instruction),"Assert Delivery Instructions not entered correctly"
        
        fill_form(driver)
        
        
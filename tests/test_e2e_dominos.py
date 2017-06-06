from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos
from tests.test_delivery_pizza_select import navigate_to_select_pizza
from tests.test_delivery_payment import navigate_to_payment
from tests.test_carryout_pizza_select import navigate_to_select_pizza
from selenium.webdriver.common.keys import Keys

def fill_form(driver):
    firstName="//*[@id='First_Name']"
    fName="Anvesh"
    Keywords.enterText(driver,fName,firstName)
    #Value not populated in the HTML page and not able to Assert if the text has been entered
    #assert (Keywords.getAttributeValue(driver,firstName)==fName),"First Name Not entered correctly"
    
    lastName="//*[@id='Last_Name']"
    lName="Malhotra"
    Keywords.enterText(driver,lName,lastName)
    Keywords.WebElement(driver,lastName).send_keys(Keys.TAB)
    #Value not populated in the HTML page and not able to Assert if the text has been entered
    #assert (Keywords.getAttributeValue(driver,lastName)==lName),"Last Name not entered correctly"
    
    email="//*[@id='Email']"
    emailAddress="test@xyz.com"
    Keywords.enterText(driver,emailAddress,email)
    Keywords.WebElement(driver,email).send_keys(Keys.TAB)
    #Value not populated in the HTML page and not able to Assert if the text has been entered
    #assert (Keywords.getAttributeValue(driver,email)==emailAddress),"Email Addres not entered correctly"
    
    
    callbackPhone="//*[@id='Callback_Phone']"
    phone="1234567890"
    Keywords.enterText(driver,phone,callbackPhone)
    Keywords.WebElement(driver,callbackPhone).send_keys(Keys.TAB)
    #Value not populated in the HTML page and not able to Assert if the text has been entered
    #assert (Keywords.getAttributeValue(driver,callbackPhone)==phone),"Phone not entered correctly"
    
    payAtStore="//*[contains(@class,'c-order-payment-cash')]"
    Keywords.ClickElement(driver,payAtStore)
    assert (Keywords.isElementSelected(driver,payAtStore)==True),"payment not selected correctly"
    

@pytest.mark.usefixtures('driver')
class TestPayment(object):
    def test_e2e_delivery_dominos(self,driver):
        navigate_to_payment(driver)
        
        deliveryInstructions="//*[@id='Delivery_Instructions']"
        instruction="Call"
        Keywords.enterText(driver,instruction,deliveryInstructions)
        Keywords.WebElement(driver,deliveryInstructions).send_keys(Keys.TAB)
        #Value not populated in the HTML page and not able to Assert if the text has been entered
        #assert (Keywords.getAttributeValue(driver,deliveryInstructions)==instruction),"Assert Delivery Instructions not entered correctly"
        fill_form(driver)
        
        #placeOrder="//*[contains(@class,'submitButton')]"
        #Keywords.ClickElement(driver,placeOrder)
        
    def test_e2e_carryout_dominos(self,driver):
        navigate_to_select_pizza(driver)
        specialityPizza="//*[contains(@class,'order-entrees-specialtypizza')]/h2"
        Keywords.ClickElement(driver,specialityPizza)
        
        order="//*[contains(@data-dpz-track-evt-name,'Order')]"
        orderElements=Keywords.WebElements(driver,order)
        
        numberOfPizza=2
        count=0
        for element in orderElements:
            if(count<numberOfPizza):
                element.click()
                addToOrder="//*[@type='submit'][contains(text(),'No, Add to Order Now')]"
                Keywords.ClickElement(driver,addToOrder)
                Keywords.isElementVisible(driver,order)
                count+=1
        cart="//*[@class='order-summary__item__title']/a"
        cartElements=Keywords.WebElements(driver,cart)
        assert (len(cartElements)==numberOfPizza),"Cart Not updated with the number of pizza's added"
        checkout="//*[contains(@class,'order-buttonCheckout-text')]"
        Keywords.ClickElement(driver,checkout)
        overlay="//*[@class='card--overlay__close js-closeButton']"
        if(len(driver.find_elements_by_xpath(overlay))>0):
            Keywords.ClickElement(driver,overlay)
        reviewOrder="//*[@class='card__title__icon'][contains(text(),'Review Order Settings')]"
        Keywords.isElementVisible(driver,reviewOrder)
        visible=len(driver.find_elements_by_xpath(reviewOrder))
        assert (visible>0),"Page not navigated after selecting pizza"
        continueCheckOut="//*[contains(@class,'js-continueCheckout')]"
        Keywords.ClickElement(driver,continueCheckOut)
        fill_form(driver)
        
        #placeOrder="//*[contains(@class,'submitButton')]"
        #Keywords.ClickElement(driver,placeOrder)
        
        
        
        
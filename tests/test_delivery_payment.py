from tests import Keywords
import pytest
from tests.Setup import navigate_to_dominos
from tests.test_delivery_pizza_select import navigate_to_select_pizza

def navigate_to_payment(driver):
    navigate_to_select_pizza(driver)
    specialityPizza="//*[contains(@class,'order-entrees-specialtypizza')]/h2"
    Keywords.ClickElement(driver,specialityPizza)
    
    order="//*[contains(@data-dpz-track-evt-name,'Order')]"
    orderElements=Keywords.WebElements(driver,order)
    
    numberOfPizza=1
    count=0
    for element in orderElements:
        if(count<numberOfPizza):
            element.click()
            addToOrder="//*[@type='submit'][contains(text(),'No, Add to Order Now')]"
            Keywords.ClickElement(driver,addToOrder)
            Keywords.isElementVisible(driver,order)
            count+=1
    checkout="//*[contains(@class,'order-buttonCheckout-text')]"
    Keywords.ClickElement(driver,checkout)
    overlay="//*[@class='card--overlay__close js-closeButton']"
    if(len(driver.find_elements_by_xpath(overlay))>0):
        Keywords.ClickElement(driver,overlay)
    continueCheckout="//*[contains(@class,'js-continueCheckout')]"
    Keywords.ClickElement(driver,continueCheckout)

@pytest.mark.usefixtures('driver')
class TestPayment(object):
    
    def test_delivery_payment_unit(self,driver):
        navigate_to_payment(driver)
        totalPrice="//*[@class='finalizedTotal js-total']"
        assert(Keywords.isElementVisible(driver,totalPrice)==True),"Total Price not calculated"
        finaltotal="//*[@class='finalizedTotal js-total']"
        totalSummary=Keywords.getText(driver,finaltotal)
        balanceDue="//*[@class='js-remainingBalanceAmount']"
        remainingBalance=Keywords.getText(driver,balanceDue)
        assert (totalSummary==remainingBalance),"Balance not equal"
    
    def test_delivery_carryout_payment_api(self,driver):
        navigate_to_payment(driver)
        placeOrder="//*[contains(@class,'js-placeOrder')]"
        Keywords.ClickElement(driver,placeOrder)
        error="This field is required."
        errorLocation=["//*[@id='First_Name-error']","//*[@id='Last_Name-error']","//*[@id='Email-error']",
                   "//*[@id='Callback_Phone-error']","//*[@id='Payment_Type-error']"
                   ]
        
        for path in errorLocation:
            assert(Keywords.getText(driver,path)==error),"Error not populated for path %s"%path  
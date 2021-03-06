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
class TestSelectPizza(object):
    
    #Verify if the user selects a coupon and the cart is empty is displayed with an error    
    def test_carryout_delivery_pizza_select_api(self,driver):
        navigate_to_select_pizza(driver)
        coupon="//*[contains(@class,'media--coupon--featured-image')]"
        Keywords.ClickElement(driver,coupon)
        close="//*[contains(@class,'js-closeButton')]"
        Keywords.ClickElement(driver,close)
        couponError="//*[@class='couponHeader__text']"
        error="COUPON INCOMPLETE"
        assert (Keywords.getText(driver,couponError)==error),"Coupon error not displayed when empty order"
    
    #Verify if the user is able to add pizza to cart    
    def test_carryout_delivery_pizza_ui_component_checkout(self,driver):   
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
        
        #Remove Item from cart
        remove="//*[contains(@class,'js-removeVariant')]"
        Keywords.ClickElement(driver,remove)
        updatedPizzaNumber=numberOfPizza-1
        newCart="//*[@class='order-summary__item__title']/a"
        newCartElements=Keywords.WebElements(driver,newCart)
        #Assertion if the item has been removed
        assert (len(newCartElements)==updatedPizzaNumber),"Cart Not updated with the number of pizza's added after deletion"
        
        #Change the quantity
        quantity="//*[@aria-label='Quantity:']"
        Keywords.ClickElement(driver,quantity)
        selectQuantity=quantity+"/option[2]"
        Keywords.ClickElement(driver,selectQuantity)
        
        checkout="//*[contains(@class,'order-buttonCheckout-text')]"
        Keywords.ClickElement(driver,checkout)
        overlay="//*[@class='card--overlay__close js-closeButton']"
        if(len(driver.find_elements_by_xpath(overlay))>0):
            Keywords.ClickElement(driver,overlay)
        reviewOrder="//*[@class='card__title__icon'][contains(text(),'Review Order Settings')]"
        Keywords.isElementVisible(driver,reviewOrder)
        visible=len(driver.find_elements_by_xpath(reviewOrder))
        assert (visible>0),"Page not navigated after selecting pizza"
        
        

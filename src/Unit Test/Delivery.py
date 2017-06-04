from common import Setup,Keywords
import string,numpy

def Deliver():
    driver=Setup.openSauceLabs("Windows-Chrome")
    print Keywords.getText(driver, "//*[contains(@class,'js-delivery')][contains(text(),'Delivery')]")
    Keywords.ClickElement(driver, "//*[contains(@class,'js-delivery')][contains(text(),'Delivery')]")
    driver.quit()
    
def DeliverUnit1():
    #Verify if the Deliver button is enabled
    driver=Setup.openSauceLabs("Windows-Chrome")
    deliveryButton="//*[contains(@class,'js-delivery')]"
    print Keywords.isElementEnabled(driver, deliveryButton)
    assert (Keywords.isElementEnabled(driver, deliveryButton) is True),"Deliver Button is not enabled"
    Keywords.ClickElement(driver, deliveryButton)
    driver.quit()
def DeliverUnit2():
    driver=Setup.openSauceLabs("Windows-Chrome")
    deliveryButton="//*[contains(@class,'js-delivery')]"
    Keywords.ClickElement(driver, deliveryButton)
    deliveryRadio="//*[@name='Service_Type'][contains(@value,'Delivery')]"
    assert (Keywords.isElementSelected(driver, deliveryRadio) is True), "Delivery Icon is not selected"
    formTitle="//*[@class='form']/div/div/h2/span"
    assert (Keywords.getText(driver, formTitle)=="IS THIS ORDER FOR DELIVERY OR CARRYOUT?"),"Form Title incorrect or missing"
    types_of_address=['Apartment','Business','Campus/Base','Hotel','Dormitory','Other']
    address="//*[@id='Address_Type_Select']/option"
    assert (Keywords.isElementVisible(driver, address) is True),"Address is not available for selection"
    addressList=Keywords.WebElements(driver, address)
    address_values=[]
    for add in addressList:
        address_values.append(add.text)
    for add in types_of_address:
        assert(add in address_values),"Address not available in list: %s"%add
    asterisk="//*[contains(@class,'requiredFieldsText')]/strong"
    requiredFields="//*[contains(@class,'requiredFieldsText')]/span"
    assert(Keywords.getText(driver, asterisk)=='*'),"asterisk is missing in required fields '*'"
    assert(Keywords.getText(driver, requiredFields)=="Indicates required field."),"Required Fields text doesn't match: %s"%"Indicates required field."
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
    driver.quit()
def DeliverUnitTypesOfAddress():
    driver=Setup.openSauceLabs("Windows-Chrome")
    deliveryButton="//*[contains(@class,'js-delivery')]"
    Keywords.ClickElement(driver, deliveryButton)
    types_of_address=['Apartment','Business','Campus/Base','Hotel','Dormitory','Other']
    address="//*[@id='Address_Type_Select']/option"
    for add in types_of_address:
        addressPath=address+"[contains(text(),'%s')]"%add
        Keywords.ClickElement(driver, addressPath)
        address_type="//*[contains(@class,'js-otherAddress')]/div[1]/label"
        assert(Keywords.getText(driver, address_type)=="Address Type:"),"Text for Address Type doesn't match: %s"%"Address Type:"
        if(add!='Campus/Base'):
            street_address="//*[@for='Street']"
            assert(Keywords.getText(driver, street_address)=="*Street Address:"),"Street address text does't match for address type: %s" % add
            city="//*[@for='City']" 
            assert(Keywords.getText(driver, city)=="*City:"),"City text doesn't match for address type: %s" % add
            state="//*[@for='Region']"
            assert(Keywords.getText(driver, state)=="*State:"),"State doesn't match for address type: %s" % add
            zip_code="//*[@for='Postal_Code']"
            assert(Keywords.getText(driver, zip_code)=="*Zip Code:"),"Zip Code doesn't match for address type: %s" % add
        location_name="//*[@for='Location_Name']"
        address_line2="//*[@for='Address_Line_2']"
        if(add=='House' or add=='Business'):
            assert(Keywords.getText(driver, address_line2)=="Suite/Apt #"),"Suite/Apt# text doesn't match expected: %s for %s" % ("Suite/Apt #",add)
        elif(add=="Apartment"):
            assert(Keywords.getText(driver, address_line2)=="*Suite/Apt #"),"Suite/Apt# doesn't match expected: %s for %s" %("*Suite/Apt #",add)
            assert(Keywords.getText(driver, location_name)=="Apartment Name"),"Apartment Name doesn't match expected: %s for %s" %("Appartment Name",add)
        elif(add=='Business'):
            assert(Keywords.getText(driver, location_name)=="Business Name"),"Business Name doesn't match expected :%s for %s" %("Business Name",add)
        elif(add=='Hotel'):
            assert(Keywords.getText(driver, location_name)=="Hotel Name"),"Hotel Name doesn't match expected :%s for %s" %("Hotel Name",add)
            assert(Keywords.getText(driver, address_line2)=="*Room #"),"Room Number doesn't match expected :%s for %s" %("*Room Number",add)
        elif(add=='Dormitory'):
            assert(Keywords.getText(driver,location_name)=="Dormitory Name"),"Dormitory Name doesn't match expected :%s for %s" %("Dormitory Name",add)
            assert(Keywords.getText(driver, address_line2)=="*Room #"),"Room # doesn't match expected :%s for %s" % ("*Room #",add)
        elif(add=='Other'):
            assert(Keywords.getText(driver, address_line2)=="Unit #"),"Unit # doesn't match expected :%s for %s" % ("Unit #",add)
        elif(add=='Campus/Base'):
            state="//*[@for='Region_Campus']"
            assert(Keywords.getText(driver, state)=='*State:'),"State doesn't match expected : %s for %s" % ("*State:",add)
            campus_base="//*[@for='Campus']"
            assert(Keywords.getText(driver, campus_base)=="*Campus/Base:"),"Campust Base doesn't match expected : %s for %s" %("*Campus/Base:",add)
            dorm="//*[@for='Dorm']"
            assert(Keywords.getText(driver, dorm)=="*Dorm/Building:"),"Dorm/Building doesn't match expected : %s for %s" %("*Dorm/Building:",add)
            dorm="//*[@for='Room_Number']"
            assert(Keywords.getText(driver, dorm)=="Room #:"),"Room # doesn't match expected : for %s for %s" %("*Room #:",add)
    driver.quit()
def DeliveryUnitEnter():
    driver=Setup.openSauceLabs("Windows-Chrome")
    deliveryButton="//*[contains(@class,'js-delivery')]"
    Keywords.ClickElement(driver, deliveryButton)
    types_of_address=['Apartment','Business','Campus/Base','Hotel','Dormitory','Other']
    address="//*[@id='Address_Type_Select']/option"
    for add in types_of_address:
        addressPath=address+"[contains(text(),'%s')]"%add
        Keywords.ClickElement(driver, addressPath)
        if(add!='Campus/Base'):
            street_address="//*[@name='Street']"
            assert (Keywords.getType(driver, street_address)=="text"),"Attribute for address is incorrect, expected :%s for %s"%("text",add)
            assert (Keywords.getAttributeLength(driver, street_address)=='40'),"Max Length for address is incorrect, expected:%s for %s"%('40',add)
            street_address_input=Keywords.generateRandom('letter', 'digits', 'punctuation', 10)
            Keywords.enterText(driver, street_address_input, street_address)
            city="//*[@name='City']"
            assert (Keywords.getType(driver, city)=="text"),"Attribute for city is incorrect, expected :%s for %s"%("text",add)
            zip_code="//*[@name='Postal_Code']"
            assert (Keywords.getType(driver, zip_code)=="tel"),"Attribute for Zip Code is incorrect,expected: %s for %s"%("tel",add)
            address_line2="//*[@name='Address_Line_2']"
            assert (Keywords.getType(driver, address_line2)=="text"),"Attribute for Address Line 2 is incorret,expected: %s for %s" %("text",add)
        if(add not in ('Campus/Base','House','Other')):
            location_name="//*[@name='Location_Name']"
            assert(Keywords.getType(driver, location_name)=='text'),"Attribute for %s Name is incorrect,expected: %s" % (add,"text")
        elif(add=='Campus/Base'):
            room_number="//*[@name='Room_Number']"
            assert (Keywords.getType(driver, room_number)=='text'),"Attribute for Room Number is incorrect, expected: %s for %s" % ("text",add)
    driver.quit()
def DeliveryUnitError():
    driver=Setup.openSauceLabs("Windows-Chrome")
    deliveryButton="//*[contains(@class,'js-delivery')]"
    Keywords.ClickElement(driver, deliveryButton)
    types_of_address=['Apartment','Business','Campus/Base','Hotel','Dormitory','Other']
    address="//*[@id='Address_Type_Select']/option"
    for add in types_of_address:
        addressPath=address+"[contains(text(),'%s')]"%add
        Keywords.ClickElement(driver, addressPath)
        submit="//*[contains(@class,'js-search-cta')]"
        Keywords.ClickElement(driver, submit)
        error="This field is required."
        if(add!='Campus/Base'):
            state_error="//*[@id='Region-error']"
            assert (Keywords.getText(driver, state_error)==error),"State Error is not the same as expected: %s for %s" %(error,add)
            postal_code_error="//*[@id='Postal_Code-error']"
            assert (Keywords.getText(driver, postal_code_error)==error),"Zip Code Error is not the same as expected: %s for %s" %(error,add)
            city_error="//*[@id='City-error']"
            assert (Keywords.getText(driver, city_error)==error), "City Error is not the same as expected: %s for %s" %(error,add)
            street_error="//*[@id='Street-error']"
            assert (Keywords.getText(driver, street_error)==error),"Street Error is not the same as expected: %s for %s" % (error,add)
        if(add in ('Apartment','Hotel','Dorm')):
            address_line2_error="//*[@id='Address_Line_2-error']"
            assert (Keywords.getText(driver, address_line2_error)==error),"Address Line error is not the same as expected: %s for %s" % (error,add)
        if(add=='Campus/Base'):
            region_campus_error="//*[@id='Region_Campus-error']"
            assert (Keywords.getText(driver, region_campus_error)==error),"State error is not the same as expected %s for %s"%(error,add)
            campus_error="//*[@id='Campus-error']"
            assert (Keywords.getText(driver, campus_error)==error),"Campus/Base error is not the same as expected %s for %s" %(error,add)
            dorm_error="//*[@id='Dorm-error']"
            assert (Keywords.getText(driver, dorm_error)==error),"Dorm Error is not the same as expected %s for %s" %(error,add)
    driver.quit()
#DeliverUnit2()
#DeliverUnitTypesOfAddress()
DeliveryUnitEnter()
#DeliveryUnitError()
#DeliverUnitTypesOfAddress()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tests import Webpage,Keywords

def navigate_to_dominos(driver):
    driver.get(Webpage.dominosURL)
    #Must be changed to a new function
    Keywords.isElementVisible(driver,"//*[contains(@class,'start-your-order')]")
    close="//*[@aria-label='Close Overlay']"
    if(len(driver.find_elements_by_xpath(close))>0):
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,close)))
            driver.find_element_by_xpath(close).click()
        #Forced to pass because by the time request is sent the element disappears
        except:
            pass
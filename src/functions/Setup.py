from selenium import webdriver

from functions import Webpage, Desktop,Keywords



def openSauceLabs(platform):
    username = "anveshmalhotra"
    authkey = "6d27c807-1c2b-41e4-9411-73944a17211e"
    saucelabconnect = "http://" + username + ":" + authkey + "@ondemand.saucelabs.com:80/wd/hub"
    if platform == "Windows-Chrome":
        capabilities = Desktop.chrome()
    elif platform == "Mac-Safari":
        capabilities = Desktop.safari()
    driver = webdriver.Remote(command_executor=saucelabconnect, desired_capabilities=capabilities)
    driver.get(Webpage.dominosURL)
    
    #Must be changed to a new function
    
    if(Keywords.isElementVisible(driver, "//*[@aria-label='Close Overlay']") is True):
        Keywords.ClickElement(driver, "//*[@aria-label='Close Overlay']")
    return driver

#driver=openSauceLabs("Windows-Chrome")
    

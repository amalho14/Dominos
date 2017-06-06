from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string,numpy


def WebElement(driver, xPath):
    return driver.find_element_by_xpath(xPath)

def WebElements(driver,xPath):
    return driver.find_elements_by_xpath(xPath)

def ClickElement(driver, xPath):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable((By.XPATH,xPath)))
    WebElement(driver, xPath).click()

def getText(driver, xPath):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, xPath)))
    return WebElement(driver, xPath).text

def isElementEnabled(driver,xPath):
    wait=WebDriverWait(driver,15)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,xPath)))
    finally:
        return WebElement(driver, xPath).is_enabled()
    
def isElementVisible(driver,xPath):
    wait=WebDriverWait(driver,15)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,xPath)))
    finally:
        return WebElement(driver, xPath).is_displayed()
    
def isElementSelected(driver,xPath):
    wait=WebDriverWait(driver,15)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,xPath)))
    finally:
        return WebElement(driver, xPath).is_selected()

def getType(driver,xPath):
    wait=WebDriverWait(driver,15)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,xPath)))
    finally:
        return WebElement(driver,xPath).get_attribute("type")
def getAttributeLength(driver,xPath):
    wait=WebDriverWait(driver,15)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,xPath)))
    finally:
        return WebElement(driver, xPath).get_attribute("maxlength")
def generateRandom(letter,digits,punctuation,size):
    chars='';
    if(letter=='letter'):
        chars+=string.letters
    if(digits=='digits'):
        chars+=string.digits
    if(punctuation=='punctuation'):
        chars+=chars+string.punctuation
    return ''.join(numpy.random.choice(list(chars), size=size))
def enterText(driver,text,xPath):
    wait=WebDriverWait(driver,15)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,xPath)))
    finally:
        WebElement(driver, xPath).clear()
        WebElement(driver, xPath).send_keys(text)
def getAttributeValue(driver,xPath):
    wait=WebDriverWait(driver,15)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,xPath)))
    finally:
        return WebElement(driver,xPath).get_attribute("value")
    
    
    
    
    
from common import Keywords,Setup
import unittest


class Deliver(unittest.TestCase):
    driver = None
    def setUp(self):
        print 'called'
        self.driver=Setup.openSauceLabs("Windows-Chrome")
    def test_1(self):
        button_text=Keywords.getText(self.driver, "//*[contains(@class,'js-delivery')][contains(text(),'Delivery')]")
        assert (button_text=='DELIVERY'),"Text of Delivery Button is incorrect, expected: %s"%'DELIVERY'
    def test_2(self):
        button_text=Keywords.getText(self.driver, "//*[contains(@class,'js-delivery')][contains(text(),'Delivery')]")
        assert (button_text=='DELIVERY'),"Text of Delivery Button is incorrect, expected: %s"%'DELIVERY'
    def test_3(self):
        button_text=Keywords.getText(self.driver, "//*[contains(@class,'js-delivery')][contains(text(),'Delivery')]")
        assert (button_text=='DELIVERY'),"Text of Delivery Button is incorrect, expected: %s"%'DELIVERY'
    def tearDown(self):
        self.driver.quit()
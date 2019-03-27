from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
import time
class LazadaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_lazada(self):
        self.driver.get("https://www.lazada.vn/")
        ids = self.driver.find_elements_by_xpath("//*[@href]")
        for id in ids:
            assert id.get_attribute('href')


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print "Complete Unit Test"


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('./report'))
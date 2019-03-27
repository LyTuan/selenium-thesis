from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Hello!")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print "Complete unistest"


if __name__ == '__main__':
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("../report/"))



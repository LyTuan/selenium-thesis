#coding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By
import  time

class TikiTestOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    def test_order(self):
        driver = self.driver
        # Here we will implement loggin into github (PART 1)
        driver.get("https://tiki.vn")
        driver.find_element_by_xpath('//span[contains(.,"Điện Thoại - Máy Tính Bảng")]').click()
        driver.find_element_by_css_selector('.product-box-list > .product-item:nth-child(2) .content').click()
        driver.find_element_by_id('#mainAddToCart').click()
        driver.find_element(By.CSS_SELECTOR,'.header-cart').click()
        time.sleep(2)
        result = driver.find_element(By.CSS_SELECTOR,'.badge-tikinow-a>.name>a').text
        self.assertIn('Điện Thoại Samsung Galaxy S10 (128GB/8GB) - Hàng Chính Hãng - Đen Ngân Hà', result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    test_main_page = unittest.TestLoader().loadTestsFromTestCase(TikiTestOrder)
    suite = unittest.TestSuite([test_main_page])
    runner = HTMLTestRunner(output='./output')
    runner.run(suite)


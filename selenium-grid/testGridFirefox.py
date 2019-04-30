#coding: utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class TikiTestOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

    def test_order(self):
        driver = self.driver
        # Here we will implement loggin into github (PART 1)
        driver.get("https://tiki.vn")
        driver.find_element_by_xpath('//span[contains(.,"Điện Thoại - Máy Tính Bảng")]').click()
        driver.find_element_by_css_selector('.product-box-list > .product-item:nth-child(2) .content').click()
        driver.find_element_by_id('#mainAddToCart').click()
        driver.find_element_by_class_name('.header-cart').click()
        self.assertIn('iPad WiFi 128GB New 2018 - Hàng Chính Hãng - Space Gray',
                        driver.find_element_by_css_selector('.badge-tikinow-a>.name>').text)
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

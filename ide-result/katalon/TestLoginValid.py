# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLoginValid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\tuanly\\PycharmProjects\\selenium-thesis\\driver\\chromedriver_73.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.lazada.vn/")
        driver.maximize_window()
        driver.find_element_by_id("anonLogin").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Phone Number or Email'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Phone Number or Email'])[1]/following::input[1]").send_keys("0389700133")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[1]").send_keys("HAPPY1524@a")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forgot Password?'])[1]/following::button[1]").click()
        self.assertEqual(u"Lý Văn Tuấn's account", driver.find_element_by_id("myAccountTrigger").text)
        driver.find_element_by_id("myAccountTrigger").click()
        driver.find_element_by_link_text("Logout").click()
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

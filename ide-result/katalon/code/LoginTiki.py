# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\admin\\Documents\\tuanlv24\\selenium\\driver\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://tiki.vn/")
        # wait for Men menu to appear, then hover it
        men_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "header-user")))
        ActionChains(driver).move_to_element(men_menu).perform()

        # wait for Fastrack menu item to appear, then click it
        fastrack = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "user-name-login")))
        fastrack.click()
        driver.find_element_by_id("popup-login-email").click()
        driver.find_element_by_id("popup-login-email").clear()
        driver.find_element_by_id("popup-login-email").send_keys("0389700133")
        driver.find_element_by_id("login_password").click()
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("zE0liV")
        driver.find_element_by_id("login_popup_submit").click()
        time.sleep(10)
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

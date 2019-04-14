import unittest
from selenium import webdriver
from src.pages import *
from src.testCases import test_cases
import time
from HtmlTestRunner import HTMLTestRunner
import pickle

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>


class TestMainPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe')
        self.driver.get("https://tiki.vn")

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    # def test_title_page(self):
    #     print("\n" + str(test_cases(6)))
    #     page = MainPage(self.driver)
    #     self.assertIn("Mua Hàng Trực Tuyến Uy Tín với Giá Rẻ Hơn tại Tiki.vn", page.get_title())
    #     # Case test fail
    #     # self.assertIn("Ly Van Tuan Test", page.get_title())
    #
    # def test_search_item(self):
    #     print("\n" + str(test_cases(1)))
    #     page = MainPage(self.driver)
    #     search_result = page.search_item("pin dell insprison 3537")
    #     self.assertIn("62 items", search_result)

    def tearDown(self):
        self.driver.close()


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe')
        self.driver.get('https://tiki.vn')

    # def test_sign_up_button(self):
    #     print("\n" + str(test_cases(2)))
    #     page = MainPage(self.driver)
    #     signUpPage = page.click_sign_up_button()
    #     self.assertIn("user/register", signUpPage.get_url())
    #
    # def test_sign_in_button(self):
    #     print("\n" + str(test_cases(3)))
    #     page = MainPage(self.driver)
    #     loginPage = page.click_sign_in_button()
    #     self.assertIn("user/login", loginPage.get_url())

    def test_sign_in_with_valid_user(self):
        print("\n" + str(test_cases(4)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_valid_user("LYTUAN")
        time.sleep(30)
        self.assertIn("tuan ly", result)

    def test_sign_in_with_in_valid_user(self):
        print("\n" + str(test_cases(5)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_in_valid_user("invalid_user")
        self.assertIn("There was a problem with your request", result)

    def tearDown(self):
        self.driver.close()


class TestCustomerCarePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe')
        self.driver.get('http://lazada.vn/')

    def test_load_customer_page(self):
        print("\n"+ str(test_cases(7)))
        customerCare = CustomerCarePage(self.driver)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    test_main_page = unittest.TestLoader().loadTestsFromTestCase(TestMainPages)
    test_login_page = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
    suite = unittest.TestSuite([test_main_page, test_login_page])
    runner = HTMLTestRunner(output='../output')
    runner.run(suite)


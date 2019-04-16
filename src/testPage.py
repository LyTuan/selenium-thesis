import unittest
from selenium import webdriver
from src.pages import *
from src.testCases import test_cases
import time
from HtmlTestRunner import HTMLTestRunner


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
    #     self.assertIn('7384'.encode('utf-8').decode('utf-8'), search_result.encode('utf-8').decode('utf-8'))

    def tearDown(self):
        self.driver.close()


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe')
        self.driver.get('https://tiki.vn')

    def test_sign_in_with_empty_email_right_password(self):
        print("\n" + str(test_cases(4)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_no_value("empty_email_right_password")
        self.assertIn("Vui lòng nhập Email hoặc Số điện thoại", result)

    def test_sign_in_with_right_email_empty_password(self):
        print("\n" + str(test_cases(5)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_in_valid_user("right_email_empty_password")
        self.assertIn("Mật khẩu không chính xác", result)

    def test_sign_in_with_in_valid_user(self):
        print("\n" + str(test_cases(6)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_no_value("empty_value")
        self.assertIn("Vui lòng nhập Email hoặc Số điện thoại", result)

    def test_sign_in_with_in_valid_email(self):
        print("\n" + str(test_cases(7)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_invalid_email("invalid_email")
        self.assertIn("Tài khoản không tồn tại", result)

    def test_sign_in_with_in_valid_password(self):
        print("\n" + str(test_cases(8)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_in_valid_user("invalid_password")
        self.assertIn("Mật khẩu không chính xác", result)

    def test_sign_in_with_valid_user(self):
        print("\n" + str(test_cases(9)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_valid_user("DoanThao")
        time.sleep(10)
        self.assertIn("Doan Phuong Thao", result)

    def tearDown(self):
        self.driver.close()


class TestCartPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe')
        self.driver.get('https://tiki.vn/')

    def test_choose_item(self):
        print("\n" + str(test_cases(9)))
        cartPage = CartPage(self.driver)
        cartPage.choose_an_item()

    # def test_delete_item(self):
    #     print("\n"+ str(test_cases(10)))



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    test_main_page = unittest.TestLoader().loadTestsFromTestCase(TestMainPages)
    test_login_page = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
    suite = unittest.TestSuite([test_main_page, test_login_page])
    # test_cart_page = unittest.TestLoader().loadTestsFromTestCase(TestCartPage)
    # suite = unittest.TestSuite([test_cart_page])
    runner = HTMLTestRunner(output='../output')
    runner.run(suite)


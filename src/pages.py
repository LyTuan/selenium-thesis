from selenium.webdriver.common.keys import Keys
from src.base import Page
from src.locators import *
from src import users
import time
# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocatars
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        time.sleep(3)
        return self.find_element(*self.locator.SEARCH_LIST).text

    def click_sign_up_button(self):
        self.hover(*self.locator.ACCOUNT)
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpPage(self.driver)

    def click_sign_in_button(self):
        self.hover(*self.locator.ACCOUNT)
        self.click(*self.locator.LOGIN)
        # self.find_element(*self.locator.LOGIN).click()
        return LoginPage(self.driver)


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocatars
        super().__init__(driver)  # Python2 version

    def enter_email(self, user):
        self.find_element(*self.locator.EMAIL).send_keys(users.get_user(user)["email"])

    def enter_password(self, user):
        self.find_element(*self.locator.PASSWORD).send_keys(users.get_user(user)["password"])

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        time.sleep(5)
        return self.find_element(*self.locator.NAME_USER).text

    def login_with_in_valid_user(self, user):
        self.login(user)
        time.sleep(5)
        return self.find_element(*self.locator.ERROR_MESSAGE).text

    def login_with_invalid_email(self, user):
        self.login(user)
        time.sleep(5)
        return self.find_element(*self.locator.ERROR_MESSAGE_EMAIL).text

    def login_with_no_value(self, user):
        self.login(user)
        time.sleep(5)
        return self.find_element(*self.locator.ERROR_MESSAGE_NO_VALUE).text

class HomePage(Page):
    pass


class SignUpPage(Page):
    pass

class CartPage(Page):
    def __init__(self, driver):
        self.locator = CartLocatars
        self.driver = driver
    def delete_an_item(self):
        self.find_element(*self.locator.CART).click()

    def choose_an_item(self):
        self.find_element(*self.locator.MAIN_NAV).click()
        self.find_element(*self.locator.ITEM).click()
        self.find_element(*self.locator.ADD_TO_CART).click()
        time.sleep(3)
        self.find_element(*self.locator.CART).click()
        return self.find_element(*self.locator.NAME_ITEM).text


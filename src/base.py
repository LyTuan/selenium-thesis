from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This Base class is serving basic attribute for every single inherited from Page class
class Page(object):
    def __init__(self, driver, base_url='http://www.app.com/'):
        self.base_url = base_url
        self.driver = driver
        self.driver.maximize_window()
        self.timout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    # def hover(self, *locator):
    #     element = self.find_element(*locator)
    #     hover = ActionChains(self.driver).move_to_element(element)
    #     hover.perform()

    def move_slider(self, *locator):
        element = self.find_element(*locator)
        width = element.size.get('width')
        xcordinate = element.location.get('x')
        print(element.location)
        # slider = ActionChains(self.driver).drag_and_drop_by_offset(element, xcordinate+width, 0)
        # slider.build().perform()
        slider = ActionChains(self.driver).click_and_hold(element).move_by_offset(width, 0)
        slider.release().perform()

    def hover(self, *locator):
        # wait for Men menu to appear, then hover it
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def click(self, *locator):
        # wait for  menu item to appear, then click it
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        element.click()

    def get_text(self, *locator):
       return self.driver.find_element(*locator).text
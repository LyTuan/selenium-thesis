from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def move_slider(self, *locator):
        element = self.find_element(*locator)
        slider = ActionChains(self.driver).click_and_hold(element)
        slider.move_by_offset(40, 0).release().perform()
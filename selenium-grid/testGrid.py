import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://127.0.0.1:4444/wd/hub',
           desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    def sign_in_to_github(self):
        driver = self.driver
        # Here we will implement loggin into github (PART 1)
        driver.get("https://github.com")
        login_in = driver.find_element_by_xpath("//a[@href='/login']")
        login_in.click()
        user = driver.find_element_by_id("login_field")
        password = driver.find_element_by_id("password")
        user.clear()
        password.clear()
        user.send_keys("lytuanduong96@gmail.com")
        password.send_keys("LYTUAN070314")
        driver.find_element_by_xpath("//input[@type='submit']").click()


    # def create_reporitory(self):
    #     driver = self.driver
    #     # Here we will implement creating repository (PART 2)
    #     new_repo_buttons = driver.find_elements_by_class_name("new-repo")
    #     if len(new_repo_buttons) > 0:
    #         new_repo_buttons[0].click()
    #     else:
    #         print("Cannot find new repository button")
    #     driver.find_element_by_name("repository[name]").send_keys("name")
    #     (driver.find_element_by_name("repository[description]")
    #      .send_keys("our new repository description"))
    #     driver.find_element_by_id("repository_auto_init").click()
    #     driver.find_element_by_xpath("//button[@type='submit']").click()


    # def delete_repository(self):
    #     driver = self.driver
    #     # Here we will implement deleting repository (PART 3)
    #     driver.find_element_by_xpath("//a[@href='/dzitkowskik/name/settings']").click()
    #     driver.implicitly_wait(5)
    #     driver.find_element_by_link_text("Delete this repository").click()
    #     (driver.find_element_by_css_selector(
    #         "div.facebox-content.dangerzone > form.js-normalize-submit > p > input[name=\"verify\"]")
    #      .clear())
    #     (driver.find_element_by_css_selector(
    #         "div.facebox-content.dangerzone > form.js-normalize-submit > p > input[name=\"verify\"]")
    #      .send_keys("name"))
    #     driver.find_element_by_xpath("(//button[@type='submit'])[5]").click()


    def test_create_delete_repository(self):
        self.sign_in_to_github()
        # self.create_reporitory()
        # self.delete_repository()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
    LOGO = (By.CLASS_NAME, 'icon-tiki_short')
    ACCOUNT = (By.ID, 'header-user')
    SIGNUP = (By.CSS_SELECTOR, '#anonSignup > a')
    LOGIN = (By.CLASS_NAME, 'user-name-login')
    SEARCH = (By.ID, 'q')
    SEARCH_LIST = (By.CLASS_NAME, 'c1DXz4')


class LoginPageLocatars(object):
    PASSWORD = (By.ID, 'login_password')
    EMAIL = (By.ID, 'popup-login-email')
    SUBMIT = (By.ID, 'login_popup_submit')
    ERROR_MESSAGE = (By.CLASS_NAME, 'help-block')
    NAME_USER = (By.CSS_SELECTOR, '#header-user >div > div > b')

class CustomerCareLocatars(object):
    CUSTOMER_CARE = (By.ID, 'topActionCustomCare')

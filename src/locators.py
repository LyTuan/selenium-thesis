from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
    LOGO = (By.CLASS_NAME, 'lzd-logo-bar')
    ACCOUNT = (By.ID, 'anonLogin')
    SIGNUP = (By.CSS_SELECTOR, '#anonSignup > a')
    LOGIN = (By.CSS_SELECTOR, '#anonLogin > a')
    SEARCH = (By.ID, 'q')
    SEARCH_LIST = (By.CLASS_NAME, 'c1DXz4')


class LoginPageLocatars(object):
    PASSWORD = (By.CSS_SELECTOR, '.mod-input-password > input')
    EMAIL = (By.CSS_SELECTOR, '.mod-input-loginName > input')
    SUBMIT = (By.CLASS_NAME, 'btn_slide')
    ERROR_MESSAGE = (By.ID, 'message_error')

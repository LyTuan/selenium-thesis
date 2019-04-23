from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
    LOGO = (By.CLASS_NAME, 'icon-tiki_short')
    ACCOUNT = (By.ID, 'header-user')
    SIGNUP = (By.CSS_SELECTOR, '#anonSignup > a')
    LOGIN = (By.CLASS_NAME, 'user-name-login')
    SEARCH = (By.NAME, 'q')
    SEARCH_LIST = (By.CSS_SELECTOR, '.filter-list-box > h4')


class LoginPageLocatars(object):
    PASSWORD = (By.ID, 'login_password')
    EMAIL = (By.ID, 'popup-login-email')
    SUBMIT = (By.ID, 'login_popup_submit')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#popup_password > .help-block')
    ERROR_MESSAGE_EMAIL = (By.CSS_SELECTOR, '#popup_login > .help-block')
    ERROR_MESSAGE_NO_VALUE = (By.CSS_SELECTOR, '#popup_login > small.help-block')
    NAME_USER = (By.CSS_SELECTOR, '#header-user > div > div > b')

class CartLocatars(object):
    CART = (By.CSS_SELECTOR, '.header-cart')
    MAIN_NAV  = (By.XPATH, '//span[contains(.,"Điện Thoại - Máy Tính Bảng")]')
    ITEM = (By.CSS_SELECTOR, '.product-box-list > .product-item:nth-child(2) .content')
    ADD_TO_CART = (By.ID, '#mainAddToCart')
    NAME_ITEM = (By.CSS_SELECTOR, '.badge-tikinow-a>.name>a')


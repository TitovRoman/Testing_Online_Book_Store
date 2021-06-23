from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class RegisterPageLocators():
    REGISTER_FORM = (By.XPATH, '//*[@id="register_form"]')
    EMAIL = (By.ID, "id_registration-email")
    PASS1 = (By.ID, "id_registration-password1")
    PASS2 = (By.ID, "id_registration-password2")
    BUTT = (By.XPATH, '//*[@id="register_form"]/button')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    NAME_PROD_PAGE = (By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE = (By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')

class CartPageLocators():
    CART = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    NOTIFICATION = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    NAME_CART_PAGE = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[2]/h3/a')
    CART_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    CONTENT_INNER = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")

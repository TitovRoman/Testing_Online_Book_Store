from selenium.webdriver.common.by import By
from .locators import ProductPageLocators, CartPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException

class Product(BasePage):
    def add_to_cart(self):
        btn_add = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        self.product_name = self.browser.find_element(*ProductPageLocators.NAME_PROD_PAGE).text
        btn_add.click() 

    def first_check_cart_items(self):
        ntf = (self.browser.find_element(*CartPageLocators.NOTIFICATION)).text
        assert self.product_name == ntf, f"Название: {ntf}, а должно быть {self.product_name}"

    def second_check_cart_items(self):
        name = (self.browser.find_element(*CartPageLocators.NAME_CART_PAGE)).text
        assert self.product_name == name, "В корзине другой товар или данный товар отсутствует"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    
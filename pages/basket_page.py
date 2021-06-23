from .base_page import BasePage
from .locators import CartPageLocators

class BasketPage(BasePage):
    def should_not_to_be_added_items(self):
        assert self.is_not_element_present(*CartPageLocators.CONTENT_INNER), \
            "Added items are presented, but should not be"
    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY), \
            "Cart is empty message is not presented, but should"
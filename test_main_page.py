from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.locators import CartPageLocators

#Файл с тест-кейсами

def test_guest_cant_see_product_in_basket_opened_from_main_page():
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/ru/")
    page.open()
    cart = page.find_element(*CartPageLocators.CART)
    cart.click()
    page = BasketPage(browser, page.browser.current_url)
    page.should_not_to_be_added_items()
    page.should_be_basket_is_empty_message()
    
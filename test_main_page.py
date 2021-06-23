import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import CartPageLocators

#Файл с тест-кейсами

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/ru/")
    page.open()
    cart = page.browser.find_element(*CartPageLocators.CART)
    cart.click()
    page = BasketPage(browser, page.browser.current_url)
    page.should_not_to_be_added_items()
    page.should_be_basket_is_empty_message()
    
import pytest
import random, time
from selenium import webdriver
from .pages.base_page import BasePage
from .pages.product_page import Product
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

#Файл с тест-кейсами

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        page.open()
        page.register_new_user("neww_uuser_" + str(random.randint(0,1000)) + "@mail.ru", 'qwertyuiopasdfghjklzxcvbnm')
        page.browser.implicitly_wait(4)
        page.should_be_authorized_user()
        yield

    def test_user_cant_see_success_message(self, browser):
        page = Product(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = Product(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.add_to_cart()               # выполняем метод страницы
        time.sleep(4)
        page.first_check_cart_items()
        page.go_to_cart()
        page.second_check_cart_items()

@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', 
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"])
def test_guest_can_add_product_to_basket(browser, link):
    page = Product(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart()               # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.first_check_cart_items()
    page.go_to_cart()
    page.second_check_cart_items()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Product(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart() 
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Product(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Product(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart() 
    page.should_dissapear_of_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Product(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_cart()
    page = BasketPage(browser, page.browser.current_url)
    page.should_not_to_be_added_items()
    page.should_be_basket_is_empty_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Product(browser, link)
    page.open()
    page.go_to_login_page()
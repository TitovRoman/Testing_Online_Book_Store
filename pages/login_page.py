from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators

class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "In URL there is no 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        if self.is_element_present(*RegisterPageLocators.REGISTER_FORM) == True:
            e_mail = self.browser.find_element(*RegisterPageLocators.EMAIL)
            e_mail.send_keys(email)
            password1 = self.browser.find_element(*RegisterPageLocators.PASS1)
            password1.send_keys(password)
            password2 = self.browser.find_element(*RegisterPageLocators.PASS2)
            password2.send_keys(password)
            button = self.browser.find_element(*RegisterPageLocators.BUTT)
            button.click()


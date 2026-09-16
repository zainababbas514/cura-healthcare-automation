from selenium.webdriver.common.by import By
from pages.appointment_page import AppointmentPage
from utils.base_class import BaseClass

class LoginPage(BaseClass):

    login_form = (By.ID, "login")
    username_input = (By.ID, "txt-username")
    password_input = (By.ID, "txt-password")
    login_button = (By.ID, "btn-login")
    login_error_message = (By.CSS_SELECTOR, ".lead.text-danger")

    def __init__(self, driver):
        self.driver = driver

    def is_login_form_visible(self):
        return (
                self.is_element_visible(self.login_form)
                and self.is_element_visible(self.username_input)
                and self.is_element_visible(self.password_input)
                and self.is_element_visible(self.login_button)
        )

    def enter_username(self, username):
        self.send_keys(self.username_input, username)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login_button(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

        return AppointmentPage(self.driver)

    def get_login_error_message(self):
        return self.find_element(self.login_error_message)

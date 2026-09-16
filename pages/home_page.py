from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.base_class import BaseClass

class HomePage(BaseClass):

    book_appointment_button = (By.CSS_SELECTOR, "a#btn-make-appointment")

    def __init__(self, driver):
        self.driver = driver

    def click_book_appointment_button(self):
        self.click(self.book_appointment_button)
        return LoginPage(self.driver)










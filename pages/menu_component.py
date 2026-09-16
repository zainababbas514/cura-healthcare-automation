from selenium.webdriver.common.by import By

from pages.history_page import HistoryPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from utils.base_class import BaseClass


class MenuComponent(BaseClass):

    menu_toggle = (By.CSS_SELECTOR, "a#menu-toggle")
    login_option = (By.XPATH, "//*[@class='sidebar-nav']//li[3]")
    logout_option = (By.XPATH, "//a[normalize-space()='Logout']")
    history_option = (By.XPATH, "//a[normalize-space()='History']")
    profile_option = (By.XPATH, "//a[normalize-space()='Profile']")
    menu_options = (By.CSS_SELECTOR, "ul.sidebar-nav li:nth-child(n+3) a")

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        self.click(self.menu_toggle)

    def click_menu_login_option(self):
        self.click(self.login_option)
        return LoginPage(self.driver)

    def click_menu_logout_option(self):
        self.click(self.logout_option)

    def click_menu_history_option(self):
        self.click(self.history_option)
        return HistoryPage(self.driver)

    def click_profile_button(self):
        self.click(self.profile_option)
        return ProfilePage(self.driver)

    def is_login_option_visible(self):
        return self.is_element_visible(self.login_option)

    def is_profile_option_visible(self):
        return self.is_element_visible(self.profile_option)

    def is_history_option_visible(self):
        return self.is_element_visible(self.history_option)

    def is_logout_option_visible(self):
        return self.is_element_visible(self.logout_option)

    def get_visible_menu_options(self):
        options = self.find_elements(self.menu_options)

        return [
            option.text
            for option in options
            if option.is_displayed()
        ]
from selenium.webdriver.common.by import By
from utils.base_class import BaseClass

class ProfilePage(BaseClass):

    profile_page_heading = (By.CSS_SELECTOR, "#profile h2")
    logout_button = (By.XPATH, "//p//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def is_profile_page_loaded(self):
        return self.is_element_visible(
            self.profile_page_heading
        )

    def click_logout_button(self):
        self.click(self.logout_button)






from selenium.webdriver.common.by import By

from utils.base_class import BaseClass


class HistoryPage(BaseClass):

    history_page_heading = (By.XPATH, "//h2[normalize-space()='History']")
    panel_heading = (By.XPATH, "(//div[@class='panel-heading'])[1]")
    facility = (By.XPATH, "(//p[@id='facility'])[1]")
    hospital_readmission = (By.XPATH, "(//p[@id='hospital_readmission'])[1]")
    health_care_program = (By.XPATH, "(//p[@id='program'])[1]")
    comment = (By.XPATH, "(//p[@id='comment'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def get_history_page_heading(self):
        return self.get_text(self.history_page_heading).strip()

    def get_visit_date(self):
        return self.get_text(self.panel_heading).strip()

    def get_facility(self):
        return self.get_text(self.facility).strip()

    def get_hospital_readmission(self):
        return self.get_text(self.hospital_readmission).strip()

    def get_healthcare_program(self):
        return self.get_text(self.health_care_program).strip()

    def get_comment(self):
        return self.get_text(self.comment).strip()
from selenium.webdriver.common.by import By

from utils.base_class import BaseClass


class AppointmentConfirmationPage(BaseClass):

    appointment_confirmation_message = (
        By.CSS_SELECTOR,
        "#summary .col-xs-12.text-center"
    )
    facility = (By.XPATH, "//p[@id='facility']")
    hospital_readmission = (By.XPATH, "//p[@id='hospital_readmission']")
    health_care_program = (By.XPATH, "//p[@id='program']")
    visit_date = (By.XPATH, "//p[@id='visit_date']")
    comment = (By.XPATH, "//p[@id='comment']")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_message(self):
        return self.get_text(
            self.appointment_confirmation_message
        ).strip()

    def get_facility(self):
        return self.get_text(self.facility).strip()

    def get_hospital_readmission(self):
        return self.get_text(
            self.hospital_readmission
        ).strip()


    def get_healthcare_program(self):
        return self.get_text(
            self.health_care_program
        ).strip()

    def get_visit_date(self):
        return self.get_text(self.visit_date).strip()

    def get_comment(self):
        return self.get_text(self.comment).strip()
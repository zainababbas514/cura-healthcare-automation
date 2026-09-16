from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.appointment_confirmation_page import AppointmentConfirmationPage
from utils.base_class import BaseClass


class AppointmentPage(BaseClass):

    appointment_section = (By.CSS_SELECTOR, "section#appointment")
    facility_dropdown = (By.ID, "combo_facility")
    hospital_readmission_checkbox = (
        By.XPATH,
        "//input[@name='hospital_readmission']"
    )
    comment_box = (By.ID, "txt_comment")
    book_appointment_button = (By.ID, "btn-book-appointment")
    visit_date_input = (By.ID, "txt_visit_date")

    datepicker = (
        By.CSS_SELECTOR,
        ".datepicker.datepicker-dropdown"
    )

    def __init__(self, driver):
        self.driver = driver

    def is_appointment_form_visible(self):
        return self.is_element_visible(self.appointment_section)

    def select_facility(self, facility):
        dropdown = Select(
            self.find_element(self.facility_dropdown)
        )

        dropdown.select_by_value(facility)

    def is_hospital_readmission_selected(self):
        checkbox = self.find_element(
            self.hospital_readmission_checkbox
        )

        return checkbox.is_selected()

    def apply_hospital_readmission(self, value):
        if value == "Yes":
            checkbox = self.find_element(
                self.hospital_readmission_checkbox
            )

            if not checkbox.is_selected():
                checkbox.click()

    def get_healthcare_program_radio(self, value):
        locator = (
            By.XPATH,
            f"//input[@value='{value}']"
        )

        return self.find_element(locator)

    def choose_healthcare_program(self, value):
        radio_button = self.get_healthcare_program_radio(value)

        if not radio_button.is_selected():
            radio_button.click()

    def is_healthcare_program_selected(self, value):
        radio_button = self.get_healthcare_program_radio(value)

        return radio_button.is_selected()

    def select_visit_date(self, visit_date):
        self.send_keys(self.visit_date_input, visit_date)

    def write_comment(self, text):
        self.send_keys(self.comment_box, text)

    def click_appointment_button(self):
        self.click(self.book_appointment_button)

        return AppointmentConfirmationPage(self.driver)

    def is_datepicker_visible(self):
        return self.is_element_visible(self.datepicker)

    def get_visit_date_validation_message(self):
        element = self.find_element(self.visit_date_input)

        return self.driver.execute_script(
            "return arguments[0].validationMessage;",
            element
        )

    def is_visit_date_valid(self):
        element = self.find_element(self.visit_date_input)

        return self.driver.execute_script(
            "return arguments[0].checkValidity();",
            element
        )
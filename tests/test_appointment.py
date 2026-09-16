import pytest
from pages.menu_component import MenuComponent
from pages.home_page import HomePage
from utils.base_class import BaseClass

@pytest.mark.usefixtures("init_browser")
class TestAppointment(BaseClass):

    logger = BaseClass.get_logger()

    # Login Credentials
    creds = BaseClass.get_data_from_json("credentials.json")
    username = creds['login_credentials']['username']
    password = creds['login_credentials']['password']

    # Test Data
    data = BaseClass.get_data_from_json("book_appointment_data.json")

    def test_book_appointment(self):
        self.logger.info(
            "Starting TC-006: Verify the user can book an appointment successfully."
        )

        home_page = HomePage(self.driver)

        facility = self.data["TC-006"]["appointment_form_data"]["facility"]
        hospital_readmission = self.data["TC-006"]["appointment_form_data"]["hospital_readmission"]
        health_care_program = self.data["TC-006"]["appointment_form_data"]["healthcare_program"]
        visit_date = self.data["TC-006"]["appointment_form_data"]["visit_date"]
        comment = self.data["TC-006"]["appointment_form_data"]["comment"]

        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()
        assert login_page.is_login_form_visible(), "Login form is not visible."

        self.logger.info(f"The user is logging in with username {self.username}")

        appointment_page = login_page.login(
            self.username,
            self.password
        )

        assert appointment_page.is_appointment_form_visible(), "Appointment form is not visible."

        current_url = self.get_current_url()
        assert "appointment" in current_url.lower(), f"Expected 'appointment' in URL, but got '{current_url}'"

        self.logger.info("The user is logged in successfully")

        self.logger.info(f"Selecting {facility} facility from the dropdown")
        appointment_page.select_facility(facility)

        self.logger.info(f"Setting hospital readmission checkbox to {hospital_readmission}")
        appointment_page.apply_hospital_readmission(hospital_readmission)

        if hospital_readmission == "Yes":
            assert appointment_page.is_hospital_readmission_selected() is True, (
                "Hospital readmission checkbox should be selected."
            )
        else:
            assert appointment_page.is_hospital_readmission_selected() is False, (
                "Hospital readmission checkbox should not be selected."
            )

        self.logger.info(
            f"Clicking {health_care_program} healthcare program radio button"
        )

        appointment_page.choose_healthcare_program(
            health_care_program
        )

        assert appointment_page.is_healthcare_program_selected(
            health_care_program
        ), (
            f"Healthcare program '{health_care_program}' "
            "was not selected."
        )

        self.logger.info(
            f"Selecting {visit_date} as visit date"
        )
        appointment_page.select_visit_date(visit_date)

        self.logger.info("Writing comment in the comment box")
        appointment_page.write_comment(comment)

        self.logger.info(
            "Submitting the book appointment form"
        )

        appointment_confirmation_page = (
            appointment_page.click_appointment_button()
        )

        confirmation_text = appointment_confirmation_page.get_confirmation_message()
        current_url = self.get_current_url()

        assert "summary" in current_url.lower(), (
            f"Expected 'summary' in URL, "
            f"but got '{current_url}'"
        )

        assert "appointment has been booked" in confirmation_text.lower(), (
            f"Expected appointment confirmation message, "
            f"but got '{confirmation_text}'"
        )

        self.logger.info(
            f"Verifying {facility} facility is selected"
        )
        actual_facility = appointment_confirmation_page.get_facility()

        assert actual_facility == facility, (
            f"Facility does not match. "
            f"Expected '{facility}', "
            f"but got '{actual_facility}'"
        )

        self.logger.info(
            f"Verifying hospital readmission is {hospital_readmission}"
        )
        actual_value = appointment_confirmation_page.get_hospital_readmission()

        assert actual_value == hospital_readmission, (
            f"Hospital readmission value does not match. "
            f"Expected '{hospital_readmission}', "
            f"but got '{actual_value}'"
        )

        self.logger.info(
            f"Verifying {health_care_program} healthcare program is selected"
        )
        actual_program = appointment_confirmation_page.get_healthcare_program()

        assert actual_program == health_care_program, (
            f"Healthcare program does not match. "
            f"Expected '{health_care_program}', "
            f"but got '{actual_program}'"
        )

        self.logger.info(
            f"Verifying {visit_date} as visit date is selected"
        )
        actual_date = appointment_confirmation_page.get_visit_date()

        assert actual_date == visit_date, (
            f"Visit date does not match. "
            f"Expected '{visit_date}', "
            f"but got '{actual_date}'"
        )

        self.logger.info(
            "Verifying comment in the comment box"
        )
        actual_comment = appointment_confirmation_page.get_comment()

        assert actual_comment == comment, (
            f"Comment does not match. "
            f"Expected '{comment}', "
            f"but got '{actual_comment}'"
        )

    def test_book_appointment_in_history(self):
        self.logger.info(
            "Starting TC-007: Verify the booked appointment appears in the "
            "History with correct details."
        )

        # Initialize page objects
        home_page = HomePage(self.driver)
        menu_component = MenuComponent(self.driver)

        facility = self.data["TC-007"]["appointment_form_data"]["facility"]
        hospital_readmission = self.data["TC-007"]["appointment_form_data"]["hospital_readmission"]
        health_care_program = self.data["TC-007"]["appointment_form_data"]["healthcare_program"]
        visit_date = self.data["TC-007"]["appointment_form_data"]["visit_date"]
        comment = self.data["TC-007"]["appointment_form_data"]["comment"]

        # Login
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()
        assert login_page.is_login_form_visible(), "Login form is not visible."

        self.logger.info(f"The user is logging in with username {self.username}")

        appointment_page = login_page.login(
            self.username,
            self.password
        )

        # Fill appointment form
        self.logger.info(
            f"Selecting {facility} facility from the dropdown"
        )
        appointment_page.select_facility(facility)

        self.logger.info(
            f"Setting hospital readmission checkbox to {hospital_readmission}"
        )
        appointment_page.apply_hospital_readmission(
            hospital_readmission
        )

        if hospital_readmission == "Yes":
            assert appointment_page.is_hospital_readmission_selected() is True, (
                "Hospital readmission checkbox should be selected."
            )
        else:
            assert appointment_page.is_hospital_readmission_selected() is False, (
                "Hospital readmission checkbox should not be selected."
            )

        self.logger.info(
            f"Clicking {health_care_program} healthcare program radio button"
        )

        appointment_page.choose_healthcare_program(
            health_care_program
        )

        assert appointment_page.is_healthcare_program_selected(
            health_care_program
        ), (
            f"Healthcare program '{health_care_program}' "
            "was not selected."
        )

        self.logger.info(
            f"Selecting {visit_date} as visit date"
        )
        appointment_page.select_visit_date(visit_date)

        self.logger.info(
            "Writing comment in the comment box"
        )
        appointment_page.write_comment(comment)

        # Submit appointment
        self.logger.info(
            "Submitting the book appointment form"
        )

        appointment_page.click_appointment_button()

        # Navigate to History
        self.logger.info(
            "Clicking the menu toggle to open the menu"
        )
        menu_component.open_menu()

        self.logger.info(
            "Clicking the 'History' option from the menu"
        )
        history_page = menu_component.click_menu_history_option()

        # Verify History page
        self.logger.info(
            "Verifying the History page is loaded successfully"
        )

        actual_heading = history_page.get_history_page_heading()

        assert actual_heading == "History", (
            f"Expected heading 'History', "
            f"but got '{actual_heading}'"
        )

        current_url = self.get_current_url()

        assert "history" in current_url.lower(), (
            f"Expected 'history' in URL, "
            f"but got '{current_url}'"
        )

        # Verify appointment details
        self.logger.info(
            f"Verifying correct {visit_date} date is showing "
            "as panel heading in the History page"
        )

        actual_visit_date = history_page.get_visit_date()

        assert actual_visit_date == visit_date, (
            f"Visit date does not match. "
            f"Expected '{visit_date}', "
            f"but got '{actual_visit_date}'"
        )

        self.logger.info(
            f"Verifying correct {facility} facility is showing "
            "inside the History panel"
        )

        actual_facility = history_page.get_facility()

        assert actual_facility == facility, (
            f"Facility does not match. "
            f"Expected '{facility}', "
            f"but got '{actual_facility}'"
        )

        self.logger.info(
            f"Verifying hospital readmission is {hospital_readmission}"
        )

        actual_hospital_readmission = (
            history_page.get_hospital_readmission()
        )

        assert actual_hospital_readmission == hospital_readmission, (
            f"Hospital readmission does not match. "
            f"Expected '{hospital_readmission}', "
            f"but got '{actual_hospital_readmission}'"
        )

        self.logger.info(
            f"Verifying {health_care_program} healthcare program is selected"
        )

        actual_healthcare_program = (
            history_page.get_healthcare_program()
        )

        assert actual_healthcare_program == health_care_program, (
            f"Healthcare program does not match. "
            f"Expected '{health_care_program}', "
            f"but got '{actual_healthcare_program}'"
        )

        self.logger.info(
            "Verifying correct comment is showing"
        )

        actual_comment = history_page.get_comment()

        assert actual_comment == comment, (
            f"Comment does not match. "
            f"Expected '{comment}', "
            f"but got '{actual_comment}'"
        )

    def test_visit_date_is_required(self):
        self.logger.info(
            "Starting TC-010: Verify the make appointment form "
            "cannot be submitted without selecting a Visit Date."
        )

        home_page = HomePage(self.driver)

        self.logger.info(
            "Clicking the Make Appointment button"
        )
        login_page = home_page.click_book_appointment_button()

        self.logger.info(f"The user is logging in with username {self.username}")

        appointment_page = login_page.login(
            self.username,
            self.password
        )

        self.logger.info(
            "Submitting the book appointment form "
            "without entering Visit Date"
        )

        appointment_page.click_appointment_button()

        self.logger.info(
            "Verifying the user is still on the appointment page"
        )

        assert appointment_page.is_appointment_form_visible(), (
            "User is no longer on the appointment page."
        )

        self.logger.info(
            "Verifying the datepicker is displayed"
        )

        assert appointment_page.is_datepicker_visible(), (
            "Date picker is not visible."
        )

        self.logger.info(
            "Verifying 'Please fill in this field' "
            "tooltip is shown below the visit date"
        )

        is_valid = appointment_page.is_visit_date_valid()
        message = appointment_page.get_visit_date_validation_message()

        assert is_valid is False, (
            "Visit Date field is incorrectly marked as valid."
        )

        assert "please fill out this field" in message.lower(), (
            f"Unexpected validation message: {message}"
        )
























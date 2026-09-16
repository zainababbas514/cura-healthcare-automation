import pytest

from pages.home_page import HomePage
from pages.menu_component import MenuComponent
from utils.base_class import BaseClass

@pytest.mark.usefixtures("init_browser")
class TestLogin(BaseClass):

    logger = BaseClass.get_logger()

    # TC-001: Verify Make Appointment displays login form
    def test_make_appointment_shows_login_form(self):
        self.logger.info(
            "Starting TC-001: Verify login form becomes visible "
            "when clicking 'Make Appointment' button."
        )

        # Initialize page object
        home_page = HomePage(self.driver)

        # Click Make Appointment
        self.logger.info(
            "Clicking the 'Make Appointment' button"
        )

        login_page = home_page.click_book_appointment_button()

        # Verify login form
        self.logger.info(
            "Verifying login form is displayed with username, "
            "password field and login button"
        )

        assert login_page.is_login_form_visible(), (
            "Login form did not appear after clicking "
            "'Make Appointment'."
        )

        self.logger.info(
            "TC-001 Passed: The login form is visible with "
            "all fields and the login button."
        )

    # TC-002: Verify Menu Login option displays login form
    def test_menu_login_option_shows_login_form(self):
        self.logger.info(
            "Starting TC-002: Verify clicking the 'Login' option "
            "from the menu displays the login form."
        )

        # Initialize page objects
        menu_component = MenuComponent(self.driver)

        # Open menu
        self.logger.info(
            "Clicking the menu toggle to open the menu"
        )

        menu_component.open_menu()

        # Click Login option
        self.logger.info(
            "Clicking the 'Login' option from the menu"
        )

        login_page = menu_component.click_menu_login_option()

        # Verify login form
        self.logger.info(
            "Verifying login form is displayed with username, "
            "password field and login button"
        )

        assert login_page.is_login_form_visible(), (
            "Login form did not appear after clicking "
            "the Login option from the menu."
        )

        self.logger.info(
            "TC-002 Passed: The login form is visible with "
            "all fields and the login button."
        )

    # TC-003, TC-004, TC-005: Verify login with different credentials
    @pytest.mark.parametrize("credentials", BaseClass.get_data_from_json("login_test_data.json").values())
    def test_login(self, credentials):

        self.logger.info(
            f"Starting login test for username: {credentials['username']} "
            f"with expected result: {credentials['expected_result']}"
        )

        # Initialize page object
        home_page = HomePage(self.driver)

        # Open login form
        self.logger.info(
            "Clicking the 'Make Appointment' button"
        )

        login_page = home_page.click_book_appointment_button()

        # Login
        self.logger.info(f"The user is logging in with username {credentials['username']}")

        appointment_page = login_page.login(
            credentials["username"],
            credentials["password"]
        )

        # Successful Login
        if credentials["expected_result"] == "success":

            self.logger.info(
                "Verifying successful login"
            )

            # Verify appointment form is displayed
            assert appointment_page.is_appointment_form_visible(), (
                "Appointment form is not visible after "
                "successful login."
            )

            # Verify URL
            current_url = self.get_current_url()

            assert "appointment" in current_url.lower(), (
                f"Expected 'appointment' in URL, "
                f"but got '{current_url}'."
            )

            self.logger.info(
                "The user logged in successfully with "
                "valid credentials."
            )

        # Failed Login
        else:

            self.logger.info(
                "Verifying login failure"
            )

            # Get login error message
            error_message = login_page.get_login_error_message()

            # Verify error message is displayed
            assert error_message.is_displayed(), (
                "Login error message is not displayed "
                "after entering invalid credentials."
            )

            # Verify error message text
            assert "Login failed!" in error_message.text, (
                f"Unexpected login error message. "
                f"Expected 'Login failed!', "
                f"but got '{error_message.text}'."
            )

            # Verify user remains on login page
            current_url = self.get_current_url()

            assert "login" in current_url.lower(), (
                f"Expected 'login' in URL after failed login, "
                f"but got '{current_url}'."
            )

            self.logger.info(
                "Login failed as expected with "
                "invalid credentials."
            )
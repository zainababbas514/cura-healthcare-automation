import pytest

from pages.home_page import HomePage
from pages.menu_component import MenuComponent
from utils.base_class import BaseClass


@pytest.mark.usefixtures("init_browser")
class TestLogout(BaseClass):

    logger = BaseClass.get_logger()

    # Login Credentials
    creds = BaseClass.get_data_from_json("credentials.json")
    username = creds["login_credentials"]["username"]
    password = creds["login_credentials"]["password"]

    # TC-008: Logout from Menu
    def test_logout_from_menu(self):
        self.logger.info(
            "Starting TC-008: Verify the user can logout "
            "from the menu."
        )

        # Initialize page objects
        home_page = HomePage(self.driver)
        menu_component = MenuComponent(self.driver)

        # Login
        self.logger.info(
            "Clicking the 'Make Appointment' button"
        )

        login_page = home_page.click_book_appointment_button()

        self.logger.info(
            f"Logging in with username {self.username}"
        )

        appointment_page = login_page.login(
            self.username,
            self.password
        )

        self.logger.info(
            "Verifying the user is logged in successfully"
        )

        assert appointment_page.is_appointment_form_visible(), (
            "Appointment form is not visible after successful login."
        )

        self.logger.info(
            "The user is logged in successfully"
        )

        # Logout from Menu
        self.logger.info(
            "Opening the menu"
        )

        menu_component.open_menu()

        self.logger.info(
            "Clicking the menu Logout option"
        )

        menu_component.click_menu_logout_option()

        # Verify Home Page after Logout
        self.logger.info(
            "Waiting for the home page to complete loading"
        )

        self.wait_for_url(
            "https://katalon-demo-cura.herokuapp.com/"
        )

        # Verify Login Form after Logout
        self.logger.info(
            "Clicking the 'Make Appointment' button"
        )

        login_page = home_page.click_book_appointment_button()

        self.logger.info(
            "Verifying login form is displayed with username, "
            "password field and login button"
        )

        assert login_page.is_login_form_visible(), (
            "Login form did not appear after clicking "
            "'Make Appointment'."
        )

        # Verify Menu Options after Logout
        self.logger.info(
            "Clicking the menu toggle to open the menu"
        )

        menu_component.open_menu()

        self.logger.info(
            "Verifying correct menu options are shown "
            "after logout"
        )

        visible_options = (
            menu_component.get_visible_menu_options()
        )

        assert "Login" in visible_options, (
            "'Login' option is not visible after logout."
        )

        assert "Home" in visible_options, (
            "'Home' option is not visible after logout."
        )

        assert "History" not in visible_options, (
            "'History' option is visible after logout."
        )

        assert "Profile" not in visible_options, (
            "'Profile' option is visible after logout."
        )

        assert "Logout" not in visible_options, (
            "'Logout' option is visible after logout."
        )

        self.logger.info(
            "TC-008 - The test passed successfully"
        )

    
    # TC-009: Logout from Profile Page
    
    def test_logout_from_profile_page(self):
        self.logger.info(
            "Starting TC-009: Verify the user can logout "
            "from the profile page."
        )

        # Initialize page objects
        home_page = HomePage(self.driver)
        menu_component = MenuComponent(self.driver)

        
        # Login
        
        self.logger.info(
            "Clicking the 'Make Appointment' button"
        )

        login_page = home_page.click_book_appointment_button()

        self.logger.info(
            f"The user is logging in with username {self.username}"
        )

        appointment_page = login_page.login(
            self.username,
            self.password
        )

        self.logger.info(
            "Verifying the user is logged in successfully"
        )

        assert appointment_page.is_appointment_form_visible(), (
            "Appointment form is not visible after successful login."
        )

        self.logger.info(
            "The user is logged in successfully"
        )

        
        # Navigate to Profile
        
        self.logger.info(
            "The user is opening the menu"
        )

        menu_component.open_menu()

        self.logger.info(
            "The user is clicking the profile page option "
            "from the menu"
        )

        profile_page = menu_component.click_profile_button()

        # Verify Profile page
        self.logger.info(
            "Verifying the Profile page is loaded"
        )

        assert profile_page.is_profile_page_loaded(), (
            "Profile page heading is not visible."
        )

        current_url = self.get_current_url()

        assert "profile" in current_url.lower(), (
            f"Expected 'profile' in URL, "
            f"but got '{current_url}'"
        )

        
        # Logout from Profile
        
        self.logger.info(
            "Clicking the logout button on the profile page"
        )

        profile_page.click_logout_button()

        self.logger.info(
            "Waiting for the home page to complete loading"
        )

        self.wait_for_url(
            "https://katalon-demo-cura.herokuapp.com/"
        )

        
        # Verify Login Form after Logout
        
        self.logger.info(
            "Clicking the 'Make Appointment' button"
        )

        login_page = home_page.click_book_appointment_button()

        self.logger.info(
            "Verifying login form is displayed with username, "
            "password field and login button"
        )

        assert login_page.is_login_form_visible(), (
            "Login form did not appear after clicking "
            "'Make Appointment'."
        )

        
        # Verify Menu Options after Logout
        self.logger.info(
            "Clicking the menu toggle to open the menu"
        )

        menu_component.open_menu()

        self.logger.info(
            "Verifying correct menu options are shown "
            "after logout"
        )

        visible_options = (
            menu_component.get_visible_menu_options()
        )

        assert "Login" in visible_options, (
            "'Login' option is not visible after logout."
        )

        assert "Home" in visible_options, (
            "'Home' option is not visible after logout."
        )

        assert "History" not in visible_options, (
            "'History' option is visible after logout."
        )

        assert "Profile" not in visible_options, (
            "'Profile' option is visible after logout."
        )

        assert "Logout" not in visible_options, (
            "'Logout' option is visible after logout."
        )

        self.logger.info(
            "TC-009 - The test passed successfully"
        )


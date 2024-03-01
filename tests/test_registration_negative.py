import time

from conftest import *
from selenium.webdriver import Keys

from core.testdata import TestData

from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


class TestRegistrationNegative:
    """
    A class of tests with negative scenarios for registration page.
    """

    def test_registration_page_negative_empty_required_fields(self, browser):
        """
        Description:
         - Negative scenario for registration page: empty required fields.
         - Browser: Chrome, Firefox (parametrized by 'browser' fixture)
         - Steps:
            - Go to page https://exchange.konomik.com/
            - Click "Зарегистрироваться"
            - In registration form click Submit button without filling required fields (name, email, password)

         Checks:
             - Error messages for all required fields (name, email, password)
             - Checkbox for user agreement indication (span has class == 'error--text')

        :param browser: fixture object for getting web driver.
        """

        main_page = MainPage(browser)

        main_page.get_page()

        time.sleep(5)

        main_page.element_click(main_page.register_link)

        page = RegistrationPage(main_page.driver)

        time.sleep(5)

        page.shadow_root_element_click(page.shadow_host, page.submit_button)

        # Check that there are 3 error messages about empty required fields
        username_error = page.shadow_root_find_element(page.shadow_host, page.error_username)
        assert 'Поле не заполнено' in username_error.text, 'The error message about empty username is absent'
        email_error = page.shadow_root_find_element(page.shadow_host, page.error_email)
        assert 'Поле не заполнено' in email_error.text, 'The error message about empty email is absent'
        password_error = page.shadow_root_find_element(page.shadow_host, page.error_password)
        assert 'Поле не заполнено' in password_error.text, 'The error message about empty password is absent'

        # Check that span has "error--text" class
        agreement_span = page.shadow_root_find_element(page.shadow_host, page.agreement_span)
        assert 'error--text' in agreement_span.get_attribute('class'), "User agreement checkbox isn't indicated"

    def test_registration_page_negative_invalid_username(self, browser):
        """
        Description:
         - Negative scenario for registration page: invalid username.
         - Browser: Chrome, Firefox (parametrized by 'browser' fixture)
         - Steps:
            - Go to page https://exchange.konomik.com/
            - Click "Зарегистрироваться"
            - In registration form enter invalid username
            - Click Submit button
            - username: parametrized username data
            - test_name: test description

         Checks:
             - Error message for username field

        :param browser: fixture object for getting web driver
        """

        main_page = MainPage(browser)

        main_page.get_page()

        time.sleep(5)

        main_page.element_click(main_page.register_link)

        page = RegistrationPage(main_page.driver)

        for testdata in TestData.username_negative:
            time.sleep(5)
            username = testdata[0]
            test_name = testdata[1]
            # Clear input field for Chrome
            page.shadow_root_enter_text(page.shadow_host, page.username, '\b' * 65)
            # Clear input field for Firefox
            page.shadow_root_enter_text(page.shadow_host, page.username, Keys.CONTROL+"a")
            page.shadow_root_enter_text(page.shadow_host, page.username, Keys.DELETE)

            page.shadow_root_enter_text(page.shadow_host, page.username, username)
            page.shadow_root_element_click(page.shadow_host, page.submit_button)

            # Check the text of error messages for username field
            username_error = page.shadow_root_find_element(page.shadow_host, page.error_username)
            assert ('Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы' in
                    username_error.text), \
                f'The error message for "username: {test_name}" test is absent'

    def test_registration_page_negative_invalid_email(self, browser):
        """
        Description:
         - Negative scenario for registration page: invalid email.
         - Browser: Chrome, Firefox (parametrized by 'browser' fixture)
         - Steps:
            - Go to page https://exchange.konomik.com/
            - Click "Зарегистрироваться"
            - In registration form enter invalid email
            - Click Submit button
            - email: parametrized email data
            - test_name: test description

         Checks:
             - Error message for email field

        :param browser: fixture object for getting web driver
        """

        main_page = MainPage(browser)

        main_page.get_page()

        time.sleep(5)

        main_page.element_click(main_page.register_link)

        page = RegistrationPage(main_page.driver)

        for testdata in TestData.email_negative:
            time.sleep(5)
            email = testdata[0]
            test_name = testdata[1]
            # Clear input field for Chrome
            page.shadow_root_enter_text(page.shadow_host, page.email, '\b' * 65)
            # Clear input field for Firefox
            page.shadow_root_enter_text(page.shadow_host, page.email, Keys.CONTROL+"a")
            page.shadow_root_enter_text(page.shadow_host, page.email, Keys.DELETE)

            page.shadow_root_enter_text(page.shadow_host, page.email, email)
            page.shadow_root_element_click(page.shadow_host, page.submit_button)

            # Check the text of error messages for email field
            email_error = page.shadow_root_find_element(page.shadow_host, page.error_email)
            assert ('Формат e-mail: somebody@somewhere.ru' in
                    email_error.text), \
                f'The error message for "email: {test_name}" test is absent'

    def test_registration_page_negative_invalid_password(self, browser):
        """
        Description:
         - Negative scenario for registration page: invalid password.
         - Browser: Chrome, Firefox (parametrized by 'browser' fixture)
         - Steps:
            - Go to page https://exchange.konomik.com/
            - Click "Зарегистрироваться"
            - In registration form enter invalid password
            - Click Submit button
            - password: parametrized password data
            - test_name: test description

         Checks:
             - Error message for password field

        :param browser: fixture object for getting web driver
        """

        main_page = MainPage(browser)

        main_page.get_page()

        time.sleep(5)

        main_page.element_click(main_page.register_link)

        page = RegistrationPage(main_page.driver)

        for testdata in TestData.password_nagative:
            time.sleep(5)
            password = testdata[0]
            test_name = testdata[1]
            # Clear input field for Chrome
            page.shadow_root_enter_text(page.shadow_host, page.password, '\b' * 65)
            # Clear input field for Firefox
            page.shadow_root_enter_text(page.shadow_host, page.password, Keys.CONTROL+"a")
            page.shadow_root_enter_text(page.shadow_host, page.password, Keys.DELETE)

            page.shadow_root_enter_text(page.shadow_host, page.password, password)
            page.shadow_root_element_click(page.shadow_host, page.submit_button)

            # Check the text of error messages for password field
            password_error = page.shadow_root_find_element(page.shadow_host, page.error_password)
            assert ('Пароль должен содержать' in password_error.text), \
                f'The error message for "password: {test_name}" test is absent'

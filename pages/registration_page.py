from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    """
    Class for Registration page
    """
    def __init__(self, driver, timeout=10):
        super().__init__(driver, '/authorization/signup', timeout)

        # The registration form is in shadow root
        self.shadow_host = (By.CSS_SELECTOR, '.remoteComponent')

        self.username = (By.CSS_SELECTOR, 'div[data-wi=user-name] input')
        self.email = (By.CSS_SELECTOR, 'div[data-wi=identificator] input')
        self.password = (By.CSS_SELECTOR, 'div[data-wi=password] input')
        self.referral_code = (By.CSS_SELECTOR, 'div[data-wi=referral] input')
        self.agreement_checkbox = (By.CSS_SELECTOR, 'div[data-wi=user-agreement] input')
        self.agreement_span = (By.CSS_SELECTOR, 'div[data-wi=user-agreement] span')

        self.submit_button = (By.CSS_SELECTOR, 'button[type=submit]')

        self.error_username = (By.CSS_SELECTOR, 'div[data-wi=user-name] div[data-wi=message] span')
        self.error_email = (By.CSS_SELECTOR, 'div[data-wi=identificator] div[data-wi=message] span')
        self.error_password = (By.CSS_SELECTOR, 'div[data-wi=password] div[data-wi=error] span')

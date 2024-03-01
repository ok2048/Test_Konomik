from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    Class for Main page
    """
    def __init__(self, driver, timeout=10):
        super().__init__(driver, '', timeout)

        self.register_link = (By.XPATH, '//a[@href="/authorization/signup"]')

        # Other elements will be described here when needed

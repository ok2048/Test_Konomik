from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    """
    Base class for PageObject
    """
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.base_url = 'https://exchange.konomik.com'
        self.url = self.base_url + url
        self.driver.implicitly_wait(timeout)

    def get_page(self):
        self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def clear_text(self, locator):
        self.find_element(locator).clear()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def element_click(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_shadow_root(self, element):
        return self.driver.execute_script('return arguments[0].shadowRoot', element)

    def shadow_root_find_element(self, shadow_locator, locator):
        shadow_host = self.find_element(shadow_locator)
        shadow_root = self.get_shadow_root(shadow_host)
        element = shadow_root.find_element(*locator)
        return element

    def shadow_root_find_elements(self, shadow_locator, locator):
        shadow_host = self.find_element(shadow_locator)
        shadow_root = self.get_shadow_root(shadow_host)
        elements = shadow_root.find_elements(*locator)
        return elements

    def shadow_root_element_click(self, parent_locator, locator):
        element = self.shadow_root_find_element(parent_locator, locator)
        element.click()

    def shadow_root_clear(self, shadow_locator, locator):
        self.shadow_root_find_element(shadow_locator, locator).clear()

    def shadow_root_enter_text(self, shadow_locator, locator, text):
        element = self.shadow_root_find_element(shadow_locator, locator)
        element.send_keys(text)

    def shadow_root_get_text(self, shadow_locator, locator):
        element = self.shadow_root_find_element(shadow_locator, locator)
        return element.text

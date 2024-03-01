import pytest
from selenium import webdriver


@pytest.fixture(scope="session", params=[webdriver.Chrome(), webdriver.Firefox()])
def browser(request):
    driver = request.param
    yield driver
    driver.quit()

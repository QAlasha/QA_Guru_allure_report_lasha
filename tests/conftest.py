import pytest
import webdriver_manager
from selene import browser


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.window_height = 1080
    browser.config.window_width = 1200
    yield

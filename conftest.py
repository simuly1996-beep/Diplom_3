import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from data.data import USER


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser: chrome or firefox"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def logged_user(driver: WebDriver | WebDriver):

    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.is_login_page_open()
    login_page.login(USER)

    return USER
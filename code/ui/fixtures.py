import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data import USERNAME, PASSWORD
from ui.pages.bag_page import BagPage
from ui.pages.base_page import BasePage
from ui.pages.books_page import BooksPage
from ui.pages.general_page import GeneralPage
from ui.pages.login_page import LoginPage
from ui.pages.order_page import OrderPage
from ui.pages.signup_page import SignupPage


class UnsupportedBrowserException(Exception):
    pass

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def general_page(driver):
    return GeneralPage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def signup_page(driver):
    return SignupPage(driver=driver)

@pytest.fixture
def books_page(driver):
    return BooksPage(driver=driver)

@pytest.fixture
def bag_page(driver):
    return BagPage(driver=driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver=driver)

@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")
        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(
            executable_path=manager.install(),
            options=options,
            desired_capabilities={'acceptInsecureCerts': True}
        )
    elif browser == 'firefox':
        manager = GeckoDriverManager(version=version)
        driver = webdriver.Firefox(executable_path=manager.install())
    else:
        raise UnsupportedBrowserException(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def login_logout(login_page, general_page):
    general_page.go_login_page()
    login_page.login(USERNAME, PASSWORD)
    yield general_page
    general_page.logout()

@pytest.fixture(scope='function')
def go_books_page(general_page):
    general_page.go_books_page()

@pytest.fixture(scope='function')
def go_bag_page(general_page):
    general_page.go_bag_page()

@pytest.fixture(scope='function')
def go_signup_page(general_page):
    general_page.go_signup_page()
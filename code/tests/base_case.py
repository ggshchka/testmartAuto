import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.bag_page import BagPage
from ui.pages.base_page import BasePage
from ui.pages.books_page import BooksPage
from ui.pages.general_page import GeneralPage
from ui.pages.login_page import LoginPage
from ui.pages.order_page import OrderPage
from ui.pages.signup_page import SignupPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.general_page: GeneralPage = request.getfixturevalue('general_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.books_page: BooksPage = request.getfixturevalue('books_page')
        self.signup_page: SignupPage = request.getfixturevalue('signup_page')
        self.bag_page: BagPage = request.getfixturevalue('bag_page')
        self.order_page: OrderPage = request.getfixturevalue('order_page')

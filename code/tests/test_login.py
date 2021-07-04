import pytest

import data
from tests.base_case import BaseCase


class TestLogin(BaseCase):

    @pytest.mark.usefixtures("login_logout")
    def test_login_url(self):
        username_on_page = self.books_page.find(self.books_page.locators.AFTER_LOGIN_GET_USERNAME).text
        assert username_on_page == data.USERNAME
        assert self.driver.current_url == self.books_page.URL


    @pytest.mark.parametrize(
        "username, password",
        [
            ('', 'testpassword1'),
            ('testusername', ''),
            ('test', 'testpassword5'),
            ('testusername', 'testpassword'),
            ('testusername', '123q'),
            ('testusername', '12345'),
            ('', ''),
        ]
    )
    def test_login_negative(self, username, password):
        self.general_page.go_login_page()
        self.login_page.login(username, password)
        assert 'Не правильный Username или Password' in self.login_page.get_error_message()

import pytest

from tests.base_case import BaseCase


class TestSignup(BaseCase):

    @pytest.mark.parametrize(
        "name, username, password, conf_password",
        [
            ('Sultan', 'sltn0', 'q1234', 'q1234'),
            ('', 'George123', 'Geo.g1', 'Geo.g1'),
            ('', '22777', '4r.@#', '4r.@#'),
        ]
    )
    def test_signup_positive(self, name, username, password, conf_password):
        self.general_page.go_signup_page()
        self.signup_page.signup(name, username, password, conf_password)
        assert 'Регистрация прошла успешно' in self.signup_page.get_success_message()


    @pytest.mark.parametrize(
        "name, username, password, conf_password",
        [
            ('Sultan', 'sltn', 'q1234', 'q1234'),
            ('', 'George123', 'Georg1', 'Georg2'),
            ('Qrwtq', 'qrwtq', '12345', '12345'),
            ('Test', 'test qwe', '12 45', '12 45'),
            ('Teqqw', 'teqqw', '123q', '123q'),
            ('', 'qrwtq2', 'wwwww', 'wwwww'),
            ('Q', '2rewq', '.....', '.....'),
            ('Kors', 'Michael', '', ''),
            ('Kors', '', 'qwe12', 'qwe12'),
            ('Kors', 'Mike', '12345qwe', ''),
            ('', 'John', '', '12345qwe'),
        ]
    )
    def test_signup_negative(self, name, username, password, conf_password):
        self.general_page.go_signup_page()
        self.signup_page.signup(name, username, password, conf_password)
        assert self.signup_page.get_error_message() != ''

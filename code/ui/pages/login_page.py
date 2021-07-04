from data import BASE_URL
from ui.locators.b_locators import LoginPageLocators
from ui.pages.general_page import GeneralPage


class LoginPage(GeneralPage):

    URL = BASE_URL + 'login'
    locators = LoginPageLocators()

    def go_signup_page_from_login_box(self):
        self.click(self.locators.GO_SIGNUP_PAGE_ANOTHER)

    def login(self, username, password):

        email_input_field = self.find(self.locators.INPUT_USERNAME)
        email_input_field.clear()
        email_input_field.send_keys(username)

        password_input_field = self.find(self.locators.INPUT_PASSWORD)
        password_input_field.clear()
        password_input_field.send_keys(password)

        self.click(self.locators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find(self.locators.ERROR_BOX).text

from data import BASE_URL
from ui.locators.b_locators import SignupPageLocators
from ui.pages.general_page import GeneralPage


class SignupPage(GeneralPage):
    URL = BASE_URL + 'signup'
    locators = SignupPageLocators()

    def go_signup_page_from_signup_box(self):
        self.click(self.locators.GO_LOGIN_PAGE_ANOTHER)

    def signup(self, name, username, password, conf_password):
        email_input_field = self.find(self.locators.INPUT_NAME)
        email_input_field.clear()
        email_input_field.send_keys(name)

        email_input_field = self.find(self.locators.INPUT_USERNAME)
        email_input_field.clear()
        email_input_field.send_keys(username)

        password_input_field = self.find(self.locators.INPUT_PASSWORD)
        password_input_field.clear()
        password_input_field.send_keys(password)

        email_input_field = self.find(self.locators.INPUT_PASSWORD_CONFIRM)
        email_input_field.clear()
        email_input_field.send_keys(conf_password)

        self.click(self.locators.SUGNUP_BUTTON)

    def get_error_message(self):
        return self.find(self.locators.ERROR_BOX, 0.2).text

    def get_success_message(self):
        return self.find(self.locators.SUCCESS_SIGNUP_BOX).text

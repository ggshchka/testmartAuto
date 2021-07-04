from data import BASE_URL
from ui.locators.b_locators import GeneralPageLocators
from ui.pages.base_page import BasePage


class GeneralPage(BasePage):

    URL = BASE_URL
    locators = GeneralPageLocators()

    def go_general_page(self):
        self.click(self.locators.GO_GENERAL_PAGE)

    def go_books_page(self):
        self.click(self.locators.GO_BOOKS_PAGE)

    def go_login_page(self):
        self.click(self.locators.GO_LOGIN_PAGE)

    def go_signup_page(self):
        self.click(self.locators.GO_SIGNUP_PAGE)

    def go_bag_page(self):
        self.click(self.locators.AFTER_LOGIN_GO_BAG_PAGE)

    def logout(self):
        self.click(self.locators.AFTER_LOGIN_LOGOUT_BUTTON)

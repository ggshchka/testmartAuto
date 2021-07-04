from data import BASE_URL
from ui.locators.b_locators import BagPageLocators
from ui.pages.general_page import GeneralPage


class BagPage(GeneralPage):

    URL = BASE_URL + 'cart'
    locators = BagPageLocators()

    def reset_count_of_books(self, cnt, num_of_article):
        count_input_field = self.find(self.locators.input_count_of_book_locator(num_of_article))
        count_input_field.clear()
        count_input_field.send_keys(cnt)
        self.click(self.locators.reset_count_of_book_button_locator(num_of_article))

    def delete_books(self, num_of_article):
        self.click(self.locators.delete_books_from_bag_button_locator(num_of_article))

    def buy_books(self):
        self.click(self.locators.BUY_BOOKS_BUTTON)

    def get_sum_of_costs(self):
        return float(self.find(self.locators.SUM_OF_COSTS).text.split(' ')[0])

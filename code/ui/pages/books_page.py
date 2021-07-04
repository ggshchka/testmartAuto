from selenium.webdriver.support import expected_conditions as EC

from data import BASE_URL
from ui.locators.b_locators import BooksPageLocators
from ui.pages.general_page import GeneralPage


class BooksPage(GeneralPage):

    URL = BASE_URL + 'books'
    locators = BooksPageLocators()

    def add_book(self, num_of_article=1):
        self.click(self.locators.add_book_locator(num_of_article))

    def get_books_names(self):
        return list(map(lambda x: x.text, self.find_all(self.locators.BOOKS_NAMES)))

    def get_books_authors(self):
        return list(map(lambda x: x.text, self.find_all(self.locators.BOOKS_AUTHORS)))

    def get_books_descriptions(self):
        return list(map(lambda x: x.text, self.find_all(self.locators.BOOKS_DESCRIPTIONS)))

    def get_books_rating(self):
        return self.find_all(self.locators.BOOKS_RATINGS)

    def get_current_costs(self):
        return list(map(lambda x: float(x.text.split(' ')[0]), self.find_all(self.locators.BOOKS_CURRENT_COSTS)))

    def get_old_costs(self):
        return list(map(lambda x: float(x.text.split(' ')[0]), self.find_all(self.locators.BOOKS_OLD_COSTS)))

    def get_books_isbn13(self):
        return list(map(lambda x: x.text.split(' ')[1], self.find_all(self.locators.BOOKS_ISBN13)))

    def get_books_isbn10(self):
        return list(map(lambda x: x.text.split(' ')[1], self.find_all(self.locators.BOOKS_ISBN10)))

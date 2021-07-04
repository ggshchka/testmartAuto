from selenium.webdriver.common.by import By


class BasePageLocators(object):
    pass


class GeneralPageLocators(BasePageLocators):
    GO_GENERAL_PAGE = (By.XPATH, "//a[@href='/']")
    GO_BOOKS_PAGE = (By.XPATH, "//a[@href='/books']")
    GO_LOGIN_PAGE = (By.XPATH, "//a[@href='/login']")
    GO_SIGNUP_PAGE = (By.XPATH, "//a[@href='/signup']")

    AFTER_LOGIN_GO_BAG_PAGE = (By.XPATH, "//a[@href='/cart']")
    AFTER_LOGIN_BAG_SIZE = (By.XPATH, "//a[@href='/cart']//span[contains(@class, 'tag')]")
    AFTER_LOGIN_LOGOUT_BUTTON = (By.CSS_SELECTOR, "#signout")
    AFTER_LOGIN_GET_USERNAME = (By.XPATH, "//div[contains(text(), 'Авторизованы как')]/span[contains(@class, 'tag')]")


class LoginPageLocators(GeneralPageLocators):
    INPUT_USERNAME = (By.CSS_SELECTOR, "#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")

    GO_SIGNUP_PAGE_ANOTHER = (By.XPATH, "//div[contains(@class, 'control')]//a[@href='/signup']")

    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit")

    ERROR_BOX = (By.CSS_SELECTOR, "#msg-error")


class SignupPageLocators(GeneralPageLocators):
    INPUT_NAME = (By.CSS_SELECTOR, "#name")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#password-confirm")

    GO_LOGIN_PAGE_ANOTHER = (By.XPATH, "//div[contains(@class, 'control')]//a[@href='/login']")

    SUGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

    ERROR_BOX = (By.CSS_SELECTOR, ".notification")
    SUCCESS_SIGNUP_BOX = (By.CSS_SELECTOR, ".message>.message-body")


class BooksPageLocators(GeneralPageLocators):
    def add_book_locator(self, num_of_article):
        loc = (By.XPATH, "//article[" + str(num_of_article) + "]//span[contains(text(), 'Добавить в корзину')]")
        return loc

    def book_current_cost_locator(self, num_of_article):
        loc = (By.XPATH, "//article[" + str(num_of_article) + "]//strong[contains(@class, 'has-text-danger')]")
        return loc

    def book_name_locator(self, num_of_article):
        loc = (By.XPATH, "//article[" + str(num_of_article) + "]//h2[contains(@class, 'title')]")
        return loc

    ADD_LAST_BOOK_TO_BAG = (By.XPATH, "(//span[contains(text(), 'Добавить в корзину')])[last()]")

    BOOKS_NAMES = (By.CSS_SELECTOR, ".media-content>.content>.title")
    BOOKS_AUTHORS = (By.CSS_SELECTOR, ".media-content>.content>.subtitle")
    BOOKS_DESCRIPTIONS = (By.CSS_SELECTOR, ".media-content>.content>:nth-child(4)")
    BOOKS_RATINGS = (By.CSS_SELECTOR, "img[alt='Book rating']")
    BOOKS_CURRENT_COSTS = (By.XPATH, "//section//strong[contains(@class, 'has-text-danger')]")
    BOOKS_OLD_COSTS = (By.XPATH, "//small[contains(text(), 'Старая цена')]/span")
    BOOKS_ISBN13 = (By.XPATH, "//strong[contains(text(), 'ISBN-13')]/..")
    BOOKS_ISBN10 = (By.XPATH, "//strong[contains(text(), 'ISBN-10')]/..")


class BagPageLocators(GeneralPageLocators):

    BUY_BOOKS_BUTTON = (By.XPATH, "//button[contains(text(), 'Купить')]")
    SUM_OF_COSTS = (By.XPATH, "//form[@action='/checkout']//strong[contains(@class, 'has-text-danger')]")
    COUNT_OF_BOOKS = (By.XPATH, "//form[@action='/checkout']//div[@class='panel-block']/p")

    def input_count_of_book_locator(self, num_of_article):
        loc = (By.XPATH, "//article[" + str(num_of_article) + "]//input[@id='input']")
        return loc

    def reset_count_of_book_button_locator(self, num_of_article):
        loc = (By.XPATH, "//article[" + str(num_of_article) + "]//button[contains(text(), 'Обновить')]")
        return loc

    def delete_books_from_bag_button_locator(self, num_of_article):
        loc = (By.XPATH, "//article[" + str(num_of_article) + "]//button[contains(text(), 'Удалить')]")
        return loc


class OrderPageLocators(GeneralPageLocators):
    ORDER_NUM = (By.XPATH, "//section//h1[@class='title']")
    ORDER_DATE = (By.XPATH, "//section//p[contains(text(), 'Заказ оформлен')]")
    DELIVERY_DATE = (By.XPATH, "//section//p[contains(text(), 'Дата доставки')]/span")

    TABLE_COLUMN_NAMES = (By.XPATH, "//table/thead//th")

    BOOK_NUMBER = (By.XPATH, "//section//table/tbody//th")
    BOOK_NAME = (By.XPATH, "//table/tbody//a[@href='/books']")
    BOOK_COUNT = (By.XPATH, "//table/tbody//td[2]")
    BOOK_COST = (By.XPATH, "//table/tbody//td[3]")

    SUM_OF_COUNT = (By.XPATH, "//table/tfoot//th[3]")
    SUM_OF_COST = (By.XPATH, "//table/tfoot//th[4]")

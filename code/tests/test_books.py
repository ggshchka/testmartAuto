from tests.base_case import BaseCase


class TestBooks(BaseCase):

    """
        Должно быть указано: название книги, автор, рейтинг, описание, текущая цена и старая цена.
    """
    def test_books_have_names(self, go_books_page):
        names = self.books_page.get_books_names()
        assert all(bool(name) for name in names)

    def test_books_have_authors(self, go_books_page):
        authors = self.books_page.get_books_authors()
        assert all(bool(author) for author in authors)

    def test_books_have_ratings(self, go_books_page):
        ratings = self.books_page.get_books_rating()
        assert all(bool(rating) for rating in ratings)

    def test_books_have_descriptions(self, go_books_page):
        descriptions = self.books_page.get_books_descriptions()
        assert all(bool(description) for description in descriptions)

    def test_books_have_current_costs(self, go_books_page):
        current_costs = self.books_page.get_current_costs()
        assert all(bool(str(current_cost)) for current_cost in current_costs)

    def test_books_have_old_costs(self, go_books_page):
        old_costs = self.books_page.get_old_costs()
        assert all(bool(str(old_cost)) for old_cost in old_costs)

    """
        Цены не могут быть меньше или равны 0.00 ₽
    """
    def test_books_cost(self, go_books_page):
        current_costs = self.books_page.get_current_costs()
        old_costs = self.books_page.get_old_costs()
        assert all(cost > 0 for cost in current_costs) and all(cost > 0 for cost in old_costs)

    """
        У каждой книги должен быть уникальный ISBN-13 номер состоящий из 13 цифр, 
        где первые три отделены дефисом от остальных.
    """
    def test_isbn13(self, go_books_page):
        isbn13_values = self.books_page.get_books_isbn13()
        first_3digits = list(map(lambda x: x.split('-')[0], isbn13_values))
        last_digits = list(map(lambda x: x.split('-')[1], isbn13_values))
        assert all('-' in isbn13 for isbn13 in isbn13_values)
        assert all((len(v) == 3 and v.isdigit()) for v in first_3digits)
        assert all((len(v) == 10 and v.isdigit()) for v in last_digits)

    """
        У каждой книги должен быть уникальный ISBN-10 номер состоящий из 10 цифр.
    """
    def test_isbn10(self, go_books_page):
        isbn10_values = self.books_page.get_books_isbn10()
        assert all((len(v) == 10 and v.isdigit()) for v in isbn10_values)


    """
        Должна быть кнопка добавить в корзину.
    """
    def test_bag_button_wo_auth(self, go_books_page):
        self.books_page.add_book(1)
        assert self.login_page.URL in self.driver.current_url

    def test_bag_button_w_auth(self, login_logout, go_books_page):
        self.books_page.add_book(1)
        cnt_of_books_on_bag = int(self.books_page.find(self.books_page.locators.AFTER_LOGIN_BAG_SIZE).text)
        assert cnt_of_books_on_bag == 1
        self.books_page.add_book(2)
        self.books_page.add_book(1)
        self.books_page.go_books_page()  # обновление страницы
        cnt_of_books_on_bag = int(self.books_page.find(self.books_page.locators.AFTER_LOGIN_BAG_SIZE).text)
        assert cnt_of_books_on_bag == 3
        # teardown
        self.books_page.go_bag_page()
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)  # очистить корзину (4 книги)

    def test_add_book_id4(self, login_logout, go_books_page):
        self.books_page.add_book(4)
        self.books_page.go_books_page()
        cnt_of_books_on_bag = int(self.books_page.find(self.books_page.locators.AFTER_LOGIN_BAG_SIZE).text)
        assert cnt_of_books_on_bag == 1
        # teardown
        self.books_page.go_bag_page()
        self.bag_page.delete_books(1)

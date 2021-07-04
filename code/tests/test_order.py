import datetime

import pytest

from tests.base_case import BaseCase


class TestOrder(BaseCase):

    """
        На странице заказа у пользователя должна отображаться номер заказа
    """
    def test_order_num(self, login_logout, go_books_page):
        # setup
        self.books_page.add_book(1)
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        order_number_info = self.order_page.get_order_num()
        numb = order_number_info.split('#')[1]

        assert 'Заказ' in order_number_info
        assert numb.isdigit()

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)

    """
        На странице заказа у пользователя должна отображаться дата и время оформления заказа
    """
    def test_order_date(self, login_logout, go_books_page):
        # setup
        self.books_page.add_book(1)
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        date_ = self.order_page.get_order_date_time()
        expected_date_format = "%d.%m.%Y %H:%M:%S"

        with pytest.raises(ValueError):
            datetime.datetime.strptime(date_, expected_date_format)

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)

    """
        На странице заказа у пользователя должна отображаться дата доставки заказа
    """
    def test_delivery_date(self, login_logout, go_books_page):
        # setup
        self.books_page.add_book(1)
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        date_ = self.order_page.get_delivery_date()
        expected_date_format = "%d-%m-%Y"

        with pytest.raises(ValueError):
            datetime.datetime.strptime(date_, expected_date_format)

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)

    """
        На странице заказа у пользователя должна отображаться 
        таблица заказа со столбцами: №, Книга, Кол-во, Стоимость.
    """
    def test_order_table_column(self, login_logout, go_books_page):
        # setup
        self.books_page.add_book(2)
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        cols = self.order_page.get_table_cols_name()

        assert len(cols) == 4
        assert '№' in cols
        assert 'Книга' in cols
        assert 'Кол-во' in cols
        assert 'Стоимость' in cols

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)

    def test_order_table_book_num(self, login_logout, go_books_page):
        # setup
        self.books_page.add_book(1)
        self.books_page.add_book(1)
        self.books_page.add_book(2)
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        nums = self.order_page.get_book_nums()

        assert len(nums) == 2
        assert (1 in nums) and (2 in nums)

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)

    def test_order_table_book_name(self, login_logout, go_books_page):
        # setup
        num_of_article = 1
        self.books_page.add_book(num_of_article)
        book_name_on_books_page = self.books_page.find(
            self.books_page.locators.book_name_locator(num_of_article)
        ).text
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        book_n = self.order_page.get_book_names()[0]

        assert book_n == book_name_on_books_page

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)

    """
        На странице заказа у пользователя должно быть поле "Итого" с суммой кол-ва и стоимости.
    """
    def test_order_sum_of_counts(self, login_logout, go_books_page):
        # setup
        self.books_page.add_book(1)
        self.books_page.add_book(1)
        self.books_page.add_book(2)
        self.books_page.add_book(3)
        self.books_page.add_book(3)
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        cnts = self.order_page.get_book_cnts()
        res_sum = self.order_page.get_sum_of_counts()

        assert sum(cnts) == res_sum

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)

    def test_order_sum_of_costs(self, login_logout, go_books_page):
        # setup
        self.books_page.add_book(1)
        self.books_page.add_book(1)
        self.books_page.add_book(2)
        self.books_page.add_book(3)
        self.books_page.add_book(3)
        self.books_page.go_bag_page()
        self.bag_page.buy_books()

        costs = self.order_page.get_book_costs()
        res_sum = self.order_page.get_sum_of_costs()

        assert sum(costs) == res_sum

        # teardown
        self.order_page.go_bag_page()
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)

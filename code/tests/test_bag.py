from tests.base_case import BaseCase


class TestBag(BaseCase):

    def test_add_book_to_bag(self, login_logout, go_books_page):
        num_of_article = 1
        self.books_page.add_book(num_of_article)
        cur_cost_on_books_page = float(self.books_page.find(
            self.books_page.locators.book_current_cost_locator(num_of_article)
        ).text.split(' ')[0])
        title_on_books_page = self.books_page.find(
            self.books_page.locators.book_name_locator(num_of_article)
        ).text
        self.books_page.go_bag_page()

        cur_cost_on_bag_page = float(self.bag_page.find(
            self.books_page.locators.book_current_cost_locator(num_of_article)
        ).text.split(' ')[0])
        title_on_bag_page = self.bag_page.find(self.books_page.locators.book_name_locator(num_of_article)).text
        assert cur_cost_on_books_page == cur_cost_on_bag_page
        assert title_on_books_page == title_on_bag_page
        # teardown
        self.bag_page.delete_books(1)


    def test_sum_of_costs(self, login_logout, go_books_page):
        num_of_articles = [1, 2, 1]
        self.books_page.add_book(num_of_articles[0])
        self.books_page.add_book(num_of_articles[1])
        self.books_page.add_book(num_of_articles[2])
        cost0 = float(self.books_page.find(
            self.books_page.locators.book_current_cost_locator(num_of_articles[0])
        ).text.split(' ')[0])
        cost1 = float(self.books_page.find(
            self.books_page.locators.book_current_cost_locator(num_of_articles[1])
        ).text.split(' ')[0])
        cost2 = float(self.books_page.find(
            self.books_page.locators.book_current_cost_locator(num_of_articles[2])
        ).text.split(' ')[0])
        self.books_page.go_bag_page()

        sum_ = self.bag_page.get_sum_of_costs()
        assert cost0 + cost1 + cost2 == sum_
        # teardown
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)


    def test_delete_book(self, login_logout, go_books_page):
        num_of_articles = [1, 2]
        self.books_page.add_book(num_of_articles[0])
        self.books_page.add_book(num_of_articles[1])
        self.books_page.go_bag_page()

        num_of_article = 1
        book_name = self.bag_page.find(self.books_page.locators.book_name_locator(num_of_article)).text
        self.bag_page.delete_books(num_of_article)
        another_book_name = self.bag_page.find(self.books_page.locators.book_name_locator(num_of_article)).text
        assert book_name != another_book_name
        # teardown
        self.bag_page.delete_books(1)
        self.bag_page.delete_books(1)


    def test_reset_count_of_books(self, login_logout, go_books_page):
        self.books_page.add_book(1)
        self.books_page.go_bag_page()

        cnt_of_books_start = int(self.bag_page.find(self.bag_page.locators.COUNT_OF_BOOKS).text.split(' ')[1][1])
        self.bag_page.reset_count_of_books(4, 1)
        cnt_of_books_end = int(self.bag_page.find(self.bag_page.locators.COUNT_OF_BOOKS).text.split(' ')[1][1])
        assert cnt_of_books_start == 1
        assert cnt_of_books_end == 4

        # teardown
        self.bag_page.delete_books(1)

from ui.locators.b_locators import OrderPageLocators
from ui.pages.general_page import GeneralPage


class OrderPage(GeneralPage):

    locators = OrderPageLocators()

    def get_order_num(self):
        return self.find(self.locators.ORDER_NUM).text

    def get_order_date_time(self):
        date_ = self.find(self.locators.ORDER_DATE).text
        return date_

    def get_delivery_date(self):
        return self.find(self.locators.DELIVERY_DATE).text

    def get_table_cols_name(self):
        return list(map(lambda x: x.text, self.find_all(self.locators.DELIVERY_DATE)))

    def get_book_nums(self):
        return list(map(lambda x: int(x.text), self.find_all(self.locators.BOOK_NUMBER)))

    def get_book_names(self):
        return list(map(lambda x: x.text, self.find_all(self.locators.BOOK_NAME)))

    def get_book_cnts(self):
        return list(map(lambda x: int(x.text), self.find_all(self.locators.BOOK_COUNT)))

    def get_book_costs(self):
        return list(map(lambda x: float(x.text), self.find_all(self.locators.BOOK_COST)))

    def get_sum_of_counts(self):
        return int(self.find(self.locators.SUM_OF_COUNT).text)

    def get_sum_of_costs(self):
        return float(self.find(self.locators.SUM_OF_COUNT).text.split(' ')[0])

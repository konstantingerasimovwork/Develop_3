import allure
from Chrome.pages.order_feed_page import OrderFeedPage
from Chrome.data import ORDERS_FEED_LINK


class TestOrderFeedPage:

    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_modal_window(self, browser):
        order_feed = OrderFeedPage(browser)
        browser.get(ORDERS_FEED_LINK)
        order_window = order_feed.open_order_modal_window()
        assert order_window.is_displayed()

    @allure.title('Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_check_order_number_in_orders_feed(self, browser, login_account):
        order_feed = OrderFeedPage(browser)
        order_feed.drag_and_drop_bun()
        order_feed.create_order()
        order_number = order_feed.get_history_of_orders()
        orders_list = order_feed.get_orders_feed_list()
        assert order_number in orders_list

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all_time_value_after_create_order(self, browser, login_account):
        order_feed = OrderFeedPage(browser)
        counter_before_order = order_feed.get_counter_all_time_value_and_create_order()
        counter_after_order = order_feed.get_counter_all_time_value()
        assert int(counter_before_order) < int(counter_after_order)

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_today_value_after_create_order(self, browser, login_account):
        order_feed = OrderFeedPage(browser)
        counter_before_order = order_feed.get_counter_today_value_and_create_order()
        counter_after_order = order_feed.get_counter_today_value()
        assert int(counter_before_order) < int(counter_after_order)

    @allure.title('Проверка: после оформления заказа его номер появляется в разделе В работе')
    def test_check_order_number_in_orders_in_progress_list(self, browser, login_account):
        order_feed = OrderFeedPage(browser)
        order_feed.drag_and_drop_bun()
        order_number = order_feed.create_order_and_get_order_number()
        order_number = f'0{order_number}'
        order_in_progress_list = order_feed.get_orders_in_progress_list(order_number)
        assert order_number in order_in_progress_list, f'{order_number} и {order_in_progress_list}'

import allure
from Firefox.pages.base_page import BasePage
from Firefox.locators.order_feed_page_locators import OrderFeedLocators as order_locators


class OrderFeedPage(BasePage):
    
    @allure.step('Открытие модального окна заказа')
    def open_order_modal_window(self):
        self.click_element(order_locators.ORDERS_ITEM)
        return self.find_element(order_locators.ORDER_MODAL_WINDOW)

    @allure.step('Перетаскивание элемента в корзину')
    def drag_and_drop_bun(self):
        source = self.find_element(order_locators.BUN)
        target = self.find_element(order_locators.BASKET)
        action = self.action_chains()
        action.drag_and_drop(source, target).perform()

    @allure.step('Создание заказа')
    def create_order(self):
        self.drag_and_drop_bun()
        self.click_element(order_locators.CREATE_ORDER_BUTTON)
        self.find_element(order_locators.CONTAINER_MODAL_WINDOW)
        self.element_to_be_clickable(order_locators.EXIT_BUTTON)
        self.click_element(order_locators.EXIT_BUTTON)

    @allure.step('Получение номера заказа из Истории заказов')
    def get_history_of_orders(self):
        self.click_element(order_locators.LK_BUTTON)
        self.visibility_of_element_located(order_locators.HISTORY_ORDERS_LINK)
        self.click_element(order_locators.HISTORY_ORDERS_LINK)
        self.visibility_of_element_located(order_locators.ORDER_NUMBER)
        return self.get_text_element(order_locators.ORDER_NUMBER)

    @allure.step('Получение списка заказов из Ленты заказов')
    def get_orders_feed_list(self):
        self.click_element(order_locators.ORDERS_BUTTON)
        self.visibility_of_element_located(order_locators.ORDERS_FEED_LIST)
        orders_list = self.find_elements(order_locators.ORDERS_FEED_LIST)
        return [order_number.text for order_number in orders_list]

    @allure.step('Получение количества заказов за всё время и создание заказа')
    def get_counter_all_time_value_and_create_order(self):
        self.click_element(order_locators.ORDERS_BUTTON)
        self.visibility_of_element_located(order_locators.COUNTER_ALL_TIME)
        count_all_time = self.get_text_element(
            order_locators.COUNTER_ALL_TIME)
        self.click_element(order_locators.CONSTRUCTOR_BUTTON)
        self.create_order()
        return count_all_time

    @allure.step('Получение количества заказов за всё время')
    def get_counter_all_time_value(self):
        self.click_element(order_locators.ORDERS_BUTTON)
        self.visibility_of_element_located(order_locators.COUNTER_ALL_TIME)
        count_all_time = self.get_text_element(order_locators.COUNTER_ALL_TIME)
        return count_all_time

    @allure.step('Получение количества заказов за сегодня и создание заказа')
    def get_counter_today_value_and_create_order(self):
        self.click_element(order_locators.ORDERS_BUTTON)
        self.visibility_of_element_located(order_locators.COUNTER_TODAY)
        count_today = self.get_text_element(
            order_locators.COUNTER_TODAY)
        self.click_element(order_locators.CONSTRUCTOR_BUTTON)
        self.create_order()
        return count_today

    @allure.step('Получение количества заказов за сегодня')
    def get_counter_today_value(self):
        self.click_element(order_locators.ORDERS_BUTTON)
        self.visibility_of_element_located(order_locators.COUNTER_TODAY)
        count_today = self.get_text_element(order_locators.COUNTER_TODAY)
        return count_today

    @allure.step('Создание заказа и получение номера заказа из модального окна')
    def create_order_and_get_order_number(self):
        self.drag_and_drop_bun()
        self.click_element(order_locators.CREATE_ORDER_BUTTON)
        self.visibility_of_element_located(
            order_locators.ORDER_NUMBER_IN_MODAL_WINDOW)
        self.text_not_to_be_present_in_element(
            order_locators.ORDER_NUMBER_IN_MODAL_WINDOW, '9999')
        order_number = self.get_text_element(
            order_locators.ORDER_NUMBER_IN_MODAL_WINDOW)
        self.element_to_be_clickable(order_locators.EXIT_BUTTON)
        self.click_element(order_locators.EXIT_BUTTON)
        return order_number

    @allure.step('Получение заказов в работе')
    def get_orders_in_progress_list(self, number):
        self.click_element(order_locators.ORDERS_BUTTON)
        self.text_to_be_present_in_element(
            order_locators.ORDERS_IN_PROGRESS_LIST, number)
        orders_list = self.find_elements(order_locators.ORDERS_IN_PROGRESS_LIST)
        return [order_number.text for order_number in orders_list]

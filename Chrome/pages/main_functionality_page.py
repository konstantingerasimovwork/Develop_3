import allure
from Chrome.pages.base_page import BasePage
from Chrome.locators.main_functionality_page_locators import MainFunctionalityPageLocators as mf
from selenium.webdriver.support import expected_conditions


class MainFunctionalityPage(BasePage):

    @allure.step('Клик по кнопке Конструктор и получение текста title')
    def click_on_constructor_button_and_get_text(self):
        self.click_element(mf.CONSTRUCTOR_BUTTON)
        self.visibility_of_element_located(mf.CONSTRUCTOR_TITLE)
        return self.get_text_element(mf.CONSTRUCTOR_TITLE)

    @allure.step('Клик по кнопке Лента заказов и получение текста title')
    def click_on_orders_feed_button_and_get_text(self):
        self.click_element(mf.ORDERS_BUTTON)
        self.visibility_of_element_located(mf.ORDERS_TITLE)
        return self.get_text_element(mf.ORDERS_TITLE)

    @allure.step('Клик по табу Соусы/Клик по ингредиенту/Поиск открытого модального окна')
    def open_modal_window_with_sauce(self):
        self.click_element(mf.SAUCES_TAB)
        self.visibility_of_element_located(mf.INGREDIENT)
        self.click_element(mf.INGREDIENT)
        return self.find_element(mf.INGREDIENT_MODAL_WINDOW)

    @allure.step('Клик по табу Соусы/Клик по ингредиенту/Поиск открытого модального окна/Закрытие окна')
    def close_modal_window(self):
        self.click_element(mf.SAUCES_TAB)
        self.visibility_of_element_located(mf.INGREDIENT)
        self.click_element(mf.INGREDIENT)
        self.visibility_of_element_located(mf.INGREDIENT_MODAL_WINDOW)
        self.find_element(mf.INGREDIENT_MODAL_WINDOW)
        self.click_element(mf.EXIT_BUTTON)
    
    @allure.step('Проверка, что модальное окно закрылось')
    def check_close_window(self):
        return expected_conditions.invisibility_of_element_located(mf.EXIT_BUTTON)

    @allure.step('Получение актуальной суммы в корзине')
    def get_actual_price(self):
        return self.get_text_element(mf.BASKET_PRICE)

    @allure.step('Перетаскивание элемента в корзину')
    def drag_and_drop_bun(self):
        source = self.find_element(mf.BUN)
        target = self.find_element(mf.BASKET)
        action = self.action_chains()
        action.drag_and_drop(source, target).perform()

    @allure.step('Создание заказа по кнопке Оформить заказ')
    def click_on_create_order_button_and_check_order_window(self):
        self.visibility_of_element_located(mf.CREATE_ORDER_BUTTON)
        self.click_element(mf.CREATE_ORDER_BUTTON)
        return self.find_element(mf.ORDER_MODAL_WINDOW)

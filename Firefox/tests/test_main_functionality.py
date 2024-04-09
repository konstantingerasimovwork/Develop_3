import allure
from Firefox.pages.main_functionality_page import MainFunctionalityPage
from Firefox.data import CONSTRUCTOR_LINK, ORDERS_FEED_LINK


class TestMainFunctionalityPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_on_constructor_button(self, browser):
        main_functionality = MainFunctionalityPage(browser)
        browser.get(ORDERS_FEED_LINK)
        result = main_functionality.click_on_constructor_button_and_get_text()
        assert result == 'Соберите бургер', f'{result}'

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_on_orders_feed_button(self, browser):
        main_functionality = MainFunctionalityPage(browser)
        browser.get(CONSTRUCTOR_LINK)
        result = main_functionality.click_on_orders_feed_button_and_get_text()
        assert result == 'Лента заказов'

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_check_open_modal_window_with_sauce(self, browser):
        main_functionality = MainFunctionalityPage(browser)
        browser.get(CONSTRUCTOR_LINK)
        modal_window = main_functionality.open_modal_window_with_sauce()
        assert modal_window.is_displayed()
    
    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_check_close_modal_window_with_sauce(self, browser):
        main_functionality = MainFunctionalityPage(browser)
        browser.get(CONSTRUCTOR_LINK)
        main_functionality.close_modal_window()
        assert main_functionality.check_close_window()

    @allure.title('Проверка: при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_change_price(self, browser):
        main_functionality = MainFunctionalityPage(browser)
        browser.get(CONSTRUCTOR_LINK)
        first_price = main_functionality.get_actual_price()
        main_functionality.drag_and_drop_bun()
        second_price = main_functionality.get_actual_price()
        assert first_price != second_price, f'Старая цена - {first_price}, новая цена - {second_price}'

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    def test_create_order_by_login_user(self, browser, login_account):
        main_functionality = MainFunctionalityPage(browser)
        main_functionality.drag_and_drop_bun()
        result = main_functionality.click_on_create_order_button_and_check_order_window()
        assert result.is_displayed()

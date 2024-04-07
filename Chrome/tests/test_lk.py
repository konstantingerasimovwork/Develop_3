import allure
from Chrome.pages.lk_page import LkPage
from Chrome.data import LK_LINK, HISTORY_LINK, LOGIN_LINK

class TestLkPage:

    @allure.step('Проверка перехода по клику на «Личный кабинет»')
    def test_click_on_lk_button(self, browser, login_account):
        lk_page = LkPage(browser)
        lk_page.click_on_lk_button()
        result = lk_page.get_link_profile()
        assert result == LK_LINK, f'{result}'

    @allure.step('Проверка перехода в раздел «История заказов»')
    def test_on_history_button(self, browser, login_account):
        lk_page = LkPage(browser)
        lk_page.click_on_lk_button()
        lk_page.click_on_history_of_orders_link()
        result = lk_page.get_link_history()
        assert result == HISTORY_LINK, f'{result}'

    @allure.step('Проверка выхода из аккаунта')
    def test_on_exit_button(self, browser, login_account):
        lk_page = LkPage(browser)
        lk_page.click_on_lk_button()
        lk_page.click_on_exit_link()
        result = lk_page.get_link_login_page()
        assert result == LOGIN_LINK, f'{result}'


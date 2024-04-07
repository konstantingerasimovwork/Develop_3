import allure
from Firefox.pages.base_page import BasePage
from Firefox.locators.lk_page_locators import LkPageLocators as lk
from Firefox.data import LK_LINK, HISTORY_LINK, LOGIN_LINK


class LkPage(BasePage):
    
    @allure.step('Клик по кнопке Личный кабинет')
    def click_on_lk_button(self):
        self.invisibility_of_element_located(lk.ERROR_ELEMENT)
        self.click_element(lk.LK_BUTTON)

    @allure.step('Получения url страницы профиля')
    def get_link_profile(self):
        self.url_to_be(LK_LINK)
        return self.current_url()

    @allure.step('Клик по пункту меню История заказов')
    def click_on_history_of_orders_link(self):
        
        self.visibility_of_element_located(lk.HISTORY_ORDERS_LINK)
        self.invisibility_of_element_located(lk.ERROR_ELEMENT)
        self.click_element(lk.HISTORY_ORDERS_LINK)

    @allure.step('Получения url страницы История заказов')
    def get_link_history(self):
        self.url_to_be(HISTORY_LINK)
        return self.current_url()

    @allure.step('Клик по пункту меню Выход')
    def click_on_exit_link(self):
        self.invisibility_of_element_located(lk.ERROR_ELEMENT)
        self.visibility_of_element_located(lk.EXIT_LINK)
        self.click_element(lk.EXIT_LINK)

    @allure.step('Получение url с страницы ЛК')
    def get_link_login_page(self):
        self.url_to_be(LOGIN_LINK)
        return self.current_url()

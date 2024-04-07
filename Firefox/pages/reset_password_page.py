import allure
from Firefox.pages.base_page import BasePage
from Firefox.locators.reset_page_locators import ResetPasswordLocators as rp
from Firefox.data import RESET_PASSWORD_LINK, FORGOT_PASSWORD_LINK, TEST_EMAIL

class ResetPasswordPage(BasePage):

    @allure.step('Нажать на кнопку "Восстановить пароль"/Проверить что url изменился и найти заголовок h2')
    def click_on_reset_password_link(self):
        self.click_element(rp.RECOVERY_LINK)
        self.url_changes(RESET_PASSWORD_LINK)
        return self.current_url()

    @allure.step('Ввести email в поле/Нажить кнопку Восстановить/Проверить что url изменился и найти заголовок h2')
    def type_email_and_click_on_recovery_button(self):
        self.click_element(rp.RECOVERY_LINK)
        self.find_element_and_type_text(rp.EMAIL_FIELD, TEST_EMAIL)
        self.click_element(rp.RECOVERY_BUTTON)
        self.url_changes(FORGOT_PASSWORD_LINK)
        return self.current_url()

    @allure.step('Кликнуть на кнопку Показать-Скрыть пароль/Проверить что поле активно')
    def check_active_status_of_password_field(self):
        self.click_element(rp.RECOVERY_LINK)
        self.url_changes(RESET_PASSWORD_LINK)
        self.find_element_and_type_text(rp.EMAIL_FIELD, TEST_EMAIL)
        self.click_element(rp.RECOVERY_BUTTON)
        self.url_changes(FORGOT_PASSWORD_LINK)
        self.click_element(rp.PASSWORD_ICON)
        password_field = self.find_element(rp.PASSWORD_FIELD)
        return password_field.get_attribute("class")

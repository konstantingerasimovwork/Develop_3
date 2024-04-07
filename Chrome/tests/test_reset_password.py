import allure
from Chrome.pages.reset_password_page import ResetPasswordPage
from Chrome.data import LOGIN_LINK, RESET_PASSWORD_LINK, FORGOT_PASSWORD_LINK

class TestResetPassword:

    @allure.step('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_on_reset_password_link(self, browser):
        reset_password = ResetPasswordPage(browser)
        browser.get(LOGIN_LINK)
        result = reset_password.click_on_reset_password_link()
        assert result == FORGOT_PASSWORD_LINK

    @allure.step('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_type_email_and_click_on_recovery_button(self, browser):
        reset_password = ResetPasswordPage(browser)
        browser.get(LOGIN_LINK)
        result = reset_password.type_email_and_click_on_recovery_button()
        assert result == RESET_PASSWORD_LINK

    @allure.step('Проверка что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_check_active_status_of_password_field(self, browser):
        reset_password = ResetPasswordPage(browser)
        browser.get(LOGIN_LINK)
        result = reset_password.check_active_status_of_password_field()
        assert "input_status_active" in result, f'{result}'

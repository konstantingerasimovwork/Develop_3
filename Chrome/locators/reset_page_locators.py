from selenium.webdriver.common.by import By

class ResetPasswordLocators:

    RECOVERY_LINK = By.XPATH, '//a[@href="/forgot-password"]'
    TITLE_RECOVERY = By.XPATH, '//h2[text()="Восстановление пароля"]'
    EMAIL_FIELD = By.NAME, 'name'
    RECOVERY_BUTTON = By.CLASS_NAME, 'button_button__33qZ0'
    PASSWORD_ICON = By.CSS_SELECTOR, '.input__icon.input__icon-action'
    PASSWORD_FIELD = By.XPATH, '//input[@type="text"]/parent::div'

# input_status_active
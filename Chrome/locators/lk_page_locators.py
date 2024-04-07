from selenium.webdriver.common.by import By

class LkPageLocators:
    
    LK_BUTTON = By.LINK_TEXT, "Личный Кабинет"
    ENTER_EMAIL = By.XPATH, './/label[text()="Email"]/following-sibling::input'
    ENTER_PASSWORD = By.XPATH, './/input[@name ="Пароль"]'
    ENTER_BUTTON = By.CLASS_NAME, 'button_button__33qZ0'
    PROFILE_LINK = By.XPATH, '//a[@href="/account/profile"]'
    HISTORY_ORDERS_LINK = By.XPATH, '//a[@href="/account/order-history"]'
    EXIT_LINK = By.CLASS_NAME, 'Account_button__14Yp3'
    ERROR_ELEMENT = By.CLASS_NAME, 'Modal_modal_overlay__x2ZCr'

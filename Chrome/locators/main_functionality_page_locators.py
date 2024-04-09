from selenium.webdriver.common.by import By

class MainFunctionalityPageLocators:

    CONSTRUCTOR_BUTTON = By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]//p[text()="Конструктор"]'
    ORDERS_BUTTON = By.XPATH, '//a[@class = "AppHeader_header__link__3D_hX"]//p[text()="Лента Заказов"]'
    CONSTRUCTOR_TITLE = By.TAG_NAME, 'h1'
    ORDERS_TITLE = By.TAG_NAME, 'h1'
    SAUCES_TAB = By.XPATH, '//span[text()="Соусы"]'
    INGREDIENT = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]'
    INGREDIENT_MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal_opened__3ISw4'
    EXIT_BUTTON = By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4")]//button'
    BUN = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    BASKET = By.CLASS_NAME, 'constructor-element_pos_top'
    BASKET_PRICE = By.CLASS_NAME, 'constructor-element__price'
    CREATE_ORDER_BUTTON = By.CLASS_NAME, 'button_button__33qZ0'
    ORDER_MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal__container__Wo2l_'
    

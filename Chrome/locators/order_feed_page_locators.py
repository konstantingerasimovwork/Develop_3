from selenium.webdriver.common.by import By

class OrderFeedLocators:

    CONSTRUCTOR_BUTTON = By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]//p[text()="Конструктор"]'
    ORDERS_BUTTON = By.XPATH, '//a[@class = "AppHeader_header__link__3D_hX"]//p[text()="Лента Заказов"]'
    ORDER_MODAL_WINDOW = By.CLASS_NAME, 'Modal_orderBox__1xWdi'
    ORDERS_ITEM = By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]/a'
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "OrderHistory_textBox__3lgbs")]//p[contains(text(), "#")]'
    ORDERS_FEED_LIST = By.XPATH, '//p[contains(text(), "#")]'
    BUN = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    BASKET = By.CLASS_NAME, 'constructor-element_pos_top'
    CREATE_ORDER_BUTTON = By.CLASS_NAME, 'button_button__33qZ0'
    CONTAINER_MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal__container__Wo2l_'
    EXIT_BUTTON = By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4")]//button'
    LK_BUTTON = By.LINK_TEXT, "Личный Кабинет"
    HISTORY_ORDERS_LINK = By.XPATH, '//a[@href="/account/order-history"]'
    COUNTER_ALL_TIME = By.XPATH, '//p[contains(text(), "Выполнено за все время")]/following-sibling::p'
    COUNTER_TODAY = By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p'
    ALL_ORDERS_DONE = By.XPATH, '//li[text()= "Все текущие заказы готовы!"]'
    ORDERS_IN_PROGRESS_LIST = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady__1YFem")]/li'
    ORDER_NUMBER_IN_MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal__title__2L34m'

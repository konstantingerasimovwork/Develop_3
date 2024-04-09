import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step('найти элемент')
    def find_element(self, locator):
        return self.browser.find_element(*locator)
    
    @allure.step('найти все элементы')
    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    @allure.step('клик по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('ожидание изменения адреса страницы')
    def url_changes(self, url):
        WebDriverWait(self.browser, 5).until(EC.url_changes(url))

    @allure.step('ожидание изменения адреса страницы')
    def url_to_be(self, url):
        WebDriverWait(self.browser, 5).until(EC.url_to_be(url))

    @allure.step('ожидание видимости элемента')
    def visibility_of_element_located(self, locator):
        WebDriverWait(self.browser, 9).until(EC.visibility_of_element_located(locator))

    @allure.step('ожидание кликабельности элемента')
    def element_to_be_clickable(self, locator):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(locator))

    @allure.step('ожидание отсутствия элемента на странице')
    def invisibility_of_element_located(self, locator):
        WebDriverWait(self.browser, 20).until(
            EC.invisibility_of_element_located(locator))
        
    @allure.step('ожидание текста на странице')
    def text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.browser, 9).until(
            EC.text_to_be_present_in_element(locator, text))
        
    @allure.step('ожидание другого текста на странице')
    def text_not_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.browser, 9).until_not(
            EC.text_to_be_present_in_element(locator, text))

    @allure.step('ввод текста в поле')
    def find_element_and_type_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текущего url')
    def current_url(self):
        return self.browser.current_url
    
    @allure.step('Получения текста элемента')
    def get_text_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Ожидание текста в атрибуте элемента')
    def text_to_be_present_in_element_attribute(self, locator, attribute, value):
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value))

    @allure.step('Инициализация Action')
    def action_chains(self):
        return ActionChains(self.browser)
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Chrome.data import URL_AUTH, LOGIN_LINK
from Chrome.helpers import user_data
from Chrome.pages.base_page import BasePage
from Chrome.locators.lk_page_locators import LkPageLocators as lk


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def registration():
    data = user_data()
    payload = {
        "email": data['email'],
        "password": data['password'],
        "name": data['name']
    }
    user_login_data = {}
    response = requests.post(f'{URL_AUTH}/register', data=payload, timeout=10)
    response_text = response.json()
    if response.status_code == 200:
        user_login_data["email"] = data['email']
        user_login_data["password"] = data['password']
    yield user_login_data
    response = requests.delete(f'{URL_AUTH}/user', timeout=10,
                               headers={'Authorization': response_text["accessToken"]})


@pytest.fixture(scope="function")
def login_account(browser, registration):
    base = BasePage(browser)
    browser.get('https://stellarburgers.nomoreparties.site/')
    base.click_element(lk.LK_BUTTON)
    base.find_element_and_type_text(lk.ENTER_EMAIL,registration['email'])
    base.find_element_and_type_text(lk.ENTER_PASSWORD, registration['password'])
    base.click_element(lk.ENTER_BUTTON)
    base.url_changes(LOGIN_LINK)

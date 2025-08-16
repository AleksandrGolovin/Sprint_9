import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pages.signin_page import SigninPage
from pages.main_page import MainPage


@allure.step('Фикстура: инициализация драйвера браузера')
@pytest.fixture
def driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f"--window-size=1400,1000")
    driver_instance = webdriver.Chrome(options=chrome_options)
    
    yield driver_instance
    
    driver_instance.quit()

@allure.step('Фикстура: инициализация объекта класса SigninPage')
@pytest.fixture
def signin_page(driver):
    return SigninPage(driver)

@allure.step('Фикстура: инициализация объекта класса MainPage')
@pytest.fixture
def main_page(driver):
    return MainPage(driver)
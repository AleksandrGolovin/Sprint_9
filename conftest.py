import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pages.main_page import MainPage
from pages.signin_page import SigninPage


@allure.step('Фикстура: инициализация драйвера браузера')
@pytest.fixture(scope="function")
def driver():
    selenoid_url = os.getenv('SELENOID_URL', 'http://localhost:4444/wd/hub')
    
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f"--window-size=1400,1000")    
    driver_instance = webdriver.Remote(
        command_executor=selenoid_url,
        options=chrome_options
    )

    yield driver_instance
    
    driver_instance.quit()

@allure.step('Фикстура: инициализация объекта класса SigninPage')
@pytest.fixture(scope="function")
def signin_page(driver):
    return SigninPage(driver)

@allure.step('Фикстура: инициализация объекта класса MainPage')
@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)
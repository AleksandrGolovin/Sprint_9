import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@allure.step('Фикстура: инициализация драйвера браузера')
@pytest.fixture(scope="function")
def driver():
    print('driver enter')
    selenoid_url = os.getenv('SELENOID_URL', 'http://localhost:4444/wd/hub')
    
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f"--window-size=1400,1000")
    # capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "128.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": False
    #     }
    # }
    
    driver_instance = webdriver.Remote(
        command_executor=selenoid_url,
        options=chrome_options
    )
    print('driver middle')
    yield driver_instance
    
    print('driver quit')
    driver_instance.quit()

# @allure.step('Фикстура: инициализация драйвера браузера')
# @pytest.fixture
# def driver():
#     chrome_options = ChromeOptions()
#     chrome_options.add_argument("--incognito")
#     chrome_options.add_argument(f"--window-size=1400,1000")
#     driver_instance = webdriver.Chrome(options=chrome_options)
    
#     yield driver_instance
    
#     driver_instance.quit()

@allure.step('Фикстура: инициализация объекта класса SigninPage')
@pytest.fixture(scope="function")
def signin_page(driver):
    from pages.signin_page import SigninPage
    return SigninPage(driver)

@allure.step('Фикстура: инициализация объекта класса MainPage')
@pytest.fixture(scope="function")
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)
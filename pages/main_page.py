import allure
from pages.base_page import BasePage
from locators.general_locators import GeneralLocators
from data import URL


class MainPage(BasePage):
    BASE_URL = URL.MAIN_PAGE
    
    @allure.step('Перейти на страницу регистрации')
    def navigate_to_signup_page(self):
        self.click_to_element(GeneralLocators.LINK_SIGNUP)
        
        from pages.signup_page import SignupPage
        destination_page = SignupPage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(GeneralLocators.LINK_SIGNUP)
        ]
        return all(conditions)
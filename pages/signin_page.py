import allure
from pages.base_page import BasePage
from locators.signin_page_locators import SigninLocators
from data import URL


class SigninPage(BasePage):
    BASE_URL = URL.SIGNIN_PAGE
    
    @allure.step('Ввести учетные данные для входа')
    def _enter_credentials_data(self, email, password):
        self.set_text_to_element(SigninLocators.INPUT_EMAIL, email)
        self.set_text_to_element(SigninLocators.INPUT_PASSWORD, password)
    
    @allure.step('Авторизоваться пользователем')
    def auth(self, email, password):
        self._enter_credentials_data(email, password)
        self.click_to_element(SigninLocators.BUTTON_ENTER)
        
        from pages.recipes_page import RecipesPage
        destination_page = RecipesPage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(SigninLocators.H1_PAGE_TITLE),
            self.find_visible_element(SigninLocators.FORM_AUTH)
        ]
        return all(conditions)
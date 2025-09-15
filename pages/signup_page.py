import allure
from pages.base_page import BasePage
from locators.signup_page_locatros import SignupLocators
from data import URL, TEST_PASSWORD
from helpers import generate_unique_email


class SignupPage(BasePage):
    BASE_URL = URL.SIGNUP_PAGE
    
    @allure.step('Ввести данные нового аккаунта')
    def _enter_account_data(self, username, email, password):
        self.set_text_to_element(SignupLocators.INPUT_FIRST_NAME, 'Test')
        self.set_text_to_element(SignupLocators.INPUT_LAST_NAME, 'User')
        self.set_text_to_element(SignupLocators.INPUT_USERNAME, username)
        self.set_text_to_element(SignupLocators.INPUT_EMAIL, email)
        self.set_text_to_element(SignupLocators.INPUT_PASSWORD, password)
    
    @allure.step('Создать аккаунт')
    def create_account(self):
        email = generate_unique_email()
        username = email.split('@')[0]
        password = TEST_PASSWORD
        self._enter_account_data(username, email, password)
        self.click_to_element(SignupLocators.BUTTON_CREATE_ACCOUNT)
        
        from pages.signin_page import SigninPage
        destination_page = SigninPage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(SignupLocators.H1_PAGE_TITLE)
        ]
        return all(conditions)
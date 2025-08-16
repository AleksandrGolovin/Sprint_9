import allure


pytest_plugins = ["conftest"]

@allure.title('Тестовые сценарии страницы регистрации')
class TestSignupPage:
    
    @allure.title('Проверка регистрации нового пользователя')
    @allure.description('Открыть главную страницу, перейти на страницу регистрации, создать новый аккаунт, проверить, что перешли на страницу логина')
    def test_signup_page_create_account_seccess(self, main_page):
        main_page.open()
        signup_page = main_page.navigate_to_signup_page()
        
        signin_page = signup_page.create_account()
        
        assert signin_page.is_loaded()
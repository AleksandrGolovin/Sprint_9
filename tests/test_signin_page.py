import allure
import pytest
from data import TEST_EMAIL, TEST_PASSWORD


@allure.title('Тестовые сценарии страницы авторизации')
class TestSigninPage:
    
    @allure.title('Проверка авторизации пользователя')
    @allure.description('Открыть страницу логина, залогиниться, проверить, что перешли на страницу рецептов')
    @pytest.mark.parametrize('email, password', [(TEST_EMAIL, TEST_PASSWORD)])
    def test_signin_page_auth_seccess(self, email, password, signin_page):
        signin_page.open()
        
        recipes_page = signin_page.auth(email, password)
        
        assert recipes_page.is_loaded()
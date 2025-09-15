import allure
import pytest
from data import TEST_EMAIL, TEST_PASSWORD


@allure.title('Тестовые сценарии страницы рецептов')
class TestRecipesPage:
    
    @allure.title('Проверка создания рецепта')
    @allure.description('Открыть страницу логина, залогиниться, создать рецепт, проверить, что рецепт создан')
    @pytest.mark.parametrize('email, password', [(TEST_EMAIL, TEST_PASSWORD)])
    def test_signin_page_auth_seccess(self, email, password, signin_page):
        signin_page.open()
        recipes_page = signin_page.auth(email, password)
        
        recipe_name = recipes_page.create_recipe()
        
        assert recipes_page.is_recipe_adding(recipe_name)
from pathlib import Path
import random
import allure
from pages.base_page import BasePage
from locators.general_locators import GeneralLocators
from locators.recipes_locators import RecipesLocators
from data import URL


class RecipesPage(BasePage):
    BASE_URL = URL.RECIPES_PAGE
    
    @allure.step('Открыть вкладку создания рецепта')
    def _open_create_recipe_tab(self):
        self.wait_for_visibility(GeneralLocators.LINK_CREATE_RECIPES)
        self.click_to_element(GeneralLocators.LINK_CREATE_RECIPES)
        self.wait_for_visibility(RecipesLocators.H1_CREATE_RECIPE_TITLE)
        
    @allure.step('Открыть вкладку создания рецепта')
    def _open_recipes_tab(self):
        self.wait_for_visibility(GeneralLocators.LINK_RECIPES)
        self.click_to_element(GeneralLocators.LINK_RECIPES)
        self.wait_for_visibility(RecipesLocators.H1_RECIPES_TITLE)
    
    @allure.step('Создать рецепт')
    def create_recipe(self):
        self._open_create_recipe_tab()
        with allure.step('Выбрать ингредиент'):
            self.set_text_to_element(RecipesLocators.INPUT_INGREDIENT_NAME, 'хлеб')
            self.wait_for_visibility(RecipesLocators.DIV_INGREDIENTS_CONTAINER)
            elements = self.find_elements(RecipesLocators.DIV_INGREDIENTS_NAMES)
            elements_count = len(elements)
            if elements_count == 0:
                raise AssertionError
            index = random.randint(0, elements_count - 1)
            element = elements[index]
            ingredient_name = element.text
            element.click()
        with allure.step('Установить количество'):
            ingredient_amount = random.randint(75, 150)
            self.set_text_to_element(RecipesLocators.INPUT_INGREDIENT_AMOUNT, ingredient_amount)
        with allure.step('Добавить ингредиент'):
            self.click_to_element(RecipesLocators.DIV_ADD_INGREDIENT)
        with allure.step('Установить время готовки'):
            cooking_time = random.randint(15,25)
            self.set_text_to_element(RecipesLocators.INPUT_COOKING_TIME, cooking_time)
        with allure.step('Установить название рецепта'):
            doneness_level = random.choice(['Слегка', 'Сильно', 'Средне', 'Безбожно', 'Безответственно', 'Легкомысленно'])
            recipe_name = f'{doneness_level} поджаренный {ingredient_name} ({ingredient_amount}/{cooking_time})'
            self.set_text_to_element(RecipesLocators.INPUT_RECIPE_NAME, recipe_name)
        with allure.step('Установить описание рецепта'):
            recipe_description = f'Взять {ingredient_name} в количестве {ingredient_amount} г., швырнуть в пламя Ородруина на {cooking_time} мин. Подавать теплым.'
            self.set_text_to_element(RecipesLocators.TEXTAREA_DESCRIPTION, recipe_description)
        with allure.step('Прикрепить файл'):
            base_dir = Path(__file__).parent.parent
            file_path = (base_dir / "assets" / "bread.png").resolve()
            self.attach_file(RecipesLocators.INPUT_FILE, str(file_path))
        with allure.step('Нажать кнопку'):
            create_recipe_button = self.find_visible_element(RecipesLocators.BUTTON_CREATE_RECIPE)
            if create_recipe_button and create_recipe_button.is_enabled():
                create_recipe_button.click()
        return recipe_name
    
    @allure.step('Проверка создания рецепта')
    def is_recipe_adding(self, recipe_name):
        by_type, locator = RecipesLocators.H1_RECIPE
        h1_recipe_title_locator = by_type, locator.format(data=recipe_name)
        conditions = [
            self.find_visible_element(RecipesLocators.DIV_SINGLE_CARD),
            self.find_visible_element(h1_recipe_title_locator)
        ]
        return all(conditions)
    
    @allure.step('Проверка условий открытия страницы')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(GeneralLocators.LINK_SIGNOUT),
            self.find_visible_element(RecipesLocators.H1_RECIPES_TITLE)
        ]
        return all(conditions)
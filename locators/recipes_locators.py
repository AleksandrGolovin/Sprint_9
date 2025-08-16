from selenium.webdriver.common.by import By


class RecipesLocators:
    H1_RECIPES_TITLE = By.XPATH, ".//h1[text()='Рецепты']"
    
    DIV_SINGLE_CARD = By.XPATH, ".//div[contains(@class, 'single-card')]"
    H1_RECIPE = By.XPATH, ".//h1[text()='{data}']"
    
    H1_CREATE_RECIPE_TITLE = By.XPATH, ".//h1[text()='Создание рецепта']"
    INPUT_RECIPE_NAME = By.XPATH, ".//div[text()='Название рецепта']/following-sibling::input"
    INPUT_INGREDIENT_NAME = By.XPATH, ".//div[text()='Ингредиенты']/following-sibling::input"
    INPUT_INGREDIENT_AMOUNT = By.XPATH, ".//input[contains(@class, 'ingredientsAmountValue')]"
    DIV_INGREDIENTS_CONTAINER = By.XPATH, ".//div[contains(@class, 'ingredientsInputs')]/div[contains(@class, 'container')]"
    DIV_INGREDIENTS_NAMES = By.XPATH, "(.//div[contains(@class, 'ingredientsInputs')]/div[contains(@class, 'container')]/div)"
    DIV_ADD_INGREDIENT = By.XPATH, ".//div[text()='Добавить ингредиент']"
    INPUT_COOKING_TIME = By.XPATH, ".//div[text()='Время приготовления']/following-sibling::input"
    TEXTAREA_DESCRIPTION = By.XPATH, ".//div[text()='Описание рецепта']/following-sibling::textarea"
    INPUT_FILE = By.XPATH, ".//input[@type='file']"
    BUTTON_CREATE_RECIPE = By.XPATH, ".//button[text()='Создать рецепт']"
    
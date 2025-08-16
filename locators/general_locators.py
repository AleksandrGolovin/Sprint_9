from selenium.webdriver.common.by import By


class GeneralLocators:
    LINK_RECIPES = By.XPATH, ".//a[text()='Рецепты']"
    LINK_SIGNIN = By.XPATH, ".//a[text()='Войти']"
    LINK_SIGNUP = By.XPATH, ".//a[text()='Создать аккаунт']"
    LINK_SIGNOUT = By.XPATH, ".//a[text()='Выход']"
    LINK_CREATE_RECIPES = By.XPATH, ".//a[text()='Создать рецепт']"
    
from selenium.webdriver.common.by import By


class SigninLocators:
    H1_PAGE_TITLE = By.XPATH, ".//h1[text()='Войти на сайт']"
    INPUT_EMAIL = By.XPATH, ".//input[@name='email']"
    INPUT_PASSWORD = By.XPATH, ".//input[@name='password']"
    BUTTON_ENTER = By.XPATH, ".//button[text()='Войти']"
    FORM_AUTH = By.XPATH, ".//form[.//input[@name='email'] and .//input[@name='password'] and .//button[text()='Войти']]"
    
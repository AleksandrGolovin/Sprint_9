from selenium.webdriver.common.by import By


class SignupLocators:
    H1_PAGE_TITLE = By.XPATH, ".//h1[text()='Регистрация']"
    INPUT_FIRST_NAME = By.XPATH, ".//input[@name='first_name']"
    INPUT_LAST_NAME = By.XPATH, ".//input[@name='last_name']"
    INPUT_USERNAME = By.XPATH, ".//input[@name='username']"
    INPUT_EMAIL = By.XPATH, ".//input[@name='email']"
    INPUT_PASSWORD = By.XPATH, ".//input[@name='password']"
    BUTTON_CREATE_ACCOUNT = By.XPATH, ".//button[text()='Создать аккаунт']"
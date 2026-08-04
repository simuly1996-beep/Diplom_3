from selenium.webdriver.common.by import By

class LoginPageLocators:

    # заголовок ленты заказа
    LOGIN_TITLE = (By.XPATH, "//h2[contains(text(),'Вход')]")

    # Кнопка Конструктор
    SIGN_UP_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")

    OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' or @type='password']")

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")\
    
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
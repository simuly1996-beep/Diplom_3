import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import LOGIN_URL

class LoginPage(BasePage):
   
    @allure.step("Открыть страницу логирования")
    def open_login_page(self):
        self.open(LOGIN_URL)

    @allure.step("дождаться загрузки страницы")   
    def is_login_page_open(self):
        self.wait_visibility(LoginPageLocators.LOGIN_TITLE)
    
    @allure.step("Клик по кнопке войти") 
    def click_sign_up(self):
        self.wait_overlay_disappear(LoginPageLocators.OVERLAY)
        self.wait_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Логирование пользователя")  
    def login(self, user):
        
        self.send_keys_in_field(LoginPageLocators.EMAIL_INPUT, (user["email"]))
        self.send_keys_in_field(LoginPageLocators.PASSWORD_INPUT,(user["password"]))
        self.wait_overlay_disappear(LoginPageLocators.OVERLAY)
        self.wait_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.click(LoginPageLocators.LOGIN_BUTTON)

import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step("Клик по кнопке лента заказов") 
    def click_feed(self):
        self.wait_overlay_disappear(MainPageLocators.OVERLAY)
        self.wait_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
   
    @allure.step("дождаться загрузки страницы")   
    def wait_main_page_loaded(self):
        self.wait_visibility(MainPageLocators.CONSTRUCTOR_TITLE)
        
    @allure.step("проверить url страницы")
    def is_main_page_url(self):
        return self.get_current_url() == BASE_URL

    @allure.step("Клик по ингредиенту булка") 
    def click_first_bun(self):
        self.wait_overlay_disappear(MainPageLocators.OVERLAY)
        self.wait_clickable(MainPageLocators.FIRST_BUN)
        self.click(MainPageLocators.FIRST_BUN)

    @allure.step("отображение окна ингредиента")
    def display_ingredient_details_title(self):
        return self.wait_visibility(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Клик по кнопке закрытия окна") 
    def click_close_button(self):
        self.wait_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("проверка что окно ингредиента закрыто")
    def is_ingredient_window_closed(self):
        return self.is_not_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)
    
    @allure.step("Получить значение счетчика ингредиента")
    def get_first_ingredient_counter(self, ingredient):
        return int(self.get_text(ingredient) or 0)
    
    @allure.step("перетащить ингредиент в конструктор")
    def drag_and_drop_first_ingredient(self, ingredient):
        self.wait_clickable(ingredient)
        self.drag_and_drop(ingredient, MainPageLocators.CONSTRUCTOR_AREA)

    @allure.step("дождаться увеличения счетчика ингредиента")
    def wait_ingredient_counter_updated(self, ingredient, count):
        self.wait_text_in_element(ingredient, count)   

    @allure.step("Собрать бургер")
    def make_burger(self, ingredient_data):
        for ingredient_locator in ingredient_data:
            self.drag_and_drop_first_ingredient(ingredient_locator)

    @allure.step("Нажать кнопку Оформить заказ")
    def click_order_button(self):
        self.wait_overlay_disappear(MainPageLocators.OVERLAY)
        self.wait_clickable(MainPageLocators.ORDER_BUTTON)
        self.click(MainPageLocators.ORDER_BUTTON)        

    @allure.step("Дождаться загрузки текущего номера заказа")
    def wait_order_number_current_loaded(self):
        self.wait_text_in_element(MainPageLocators.ORDER_NUMBER,"9999")
        self.wait.until( lambda driver: self.get_text(MainPageLocators.ORDER_NUMBER) != "9999")
        self.wait_overlay_disappear(MainPageLocators.OVERLAY)
    
    @allure.step("Дождаться закрытия окна заказа")
    def wait_order_modal_closed(self):
        self.is_not_visible(MainPageLocators.ORDER_NUMBER)

    @allure.step("Клик по кнопке закрытия окна") 
    def click_close_button_order1(self):
        self.wait_overlay_disappear(MainPageLocators.OVERLAY)
        self.wait_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Клик по кнопке закрытия окна оформления заказа")
    def click_close_button_order(self):

        self.wait.until(EC.visibility_of_element_located(MainPageLocators.MODAL_CLOSE_BUTTON))

        for _ in range(5):
            try:
                self.wait.until(EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON))
                self.driver.find_element(*MainPageLocators.MODAL_CLOSE_BUTTON).click()
                return
            except ElementClickInterceptedException:
                time.sleep(0.3)

        raise AssertionError("Не удалось кликнуть кнопку закрытия модалки")
    
    @allure.step("Вернуть значение счетчика выполнено за день")
    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)
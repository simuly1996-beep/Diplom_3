import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from urls import FEED_URL


class FeedPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_feed_page(self):
        self.open(FEED_URL)

    @allure.step("Клик по конструктору") 
    def click_constructor(self):
        self.wait_overlay_disappear(FeedPageLocators.OVERLAY)
        self.wait_clickable(FeedPageLocators.CONSTRUCTOR_BUTTON)
        self.click(FeedPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("дождаться загрузки страницы")   
    def wait_feed_page_loaded(self):
        self.wait_visibility(FeedPageLocators.FEED_TITLE)

    @allure.step("проверить url страницы") 
    def is_feed_page_url(self):
        return self.get_current_url() == FEED_URL
    
    @allure.step("Вернуть значение счетчика выполнено за все время")
    def get_total_orders(self):
        return int(self.get_text(FeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Вернуть значение счетчика выполнено за день")
    def get_day_orders(self):
        return int(self.get_text(FeedPageLocators.DAY_ORDERS_COUNTER)) 
          
    @allure.step("Дождаться загрузки текущего номера заказа в блоке в работе")
    def wait_in_work_current_loaded(self):
        self.wait_text_in_element(FeedPageLocators.ORDER_ITEMS_IN_WORK,"Все текущие заказы готовы!")
        self.wait.until( lambda driver: self.get_text(FeedPageLocators.ORDER_ITEMS_IN_WORK) != "Все текущие заказы готовы!")
        self.wait_overlay_disappear(FeedPageLocators.OVERLAY)

    @allure.step("Вернуть значение счетчика выполнено за день")
    def get_in_work_order(self):
        order_number = str(self.get_text(FeedPageLocators.ORDER_ITEMS_IN_WORK))
        return str(order_number).lstrip("0") 
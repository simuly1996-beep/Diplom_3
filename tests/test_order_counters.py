import allure

from data.data import INGREDIENTS
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestOrdersCounter:
    
    @allure.title("Проверка увелечения счетчика Выполнено за все время")    
    def test_total_orders_counter_increases(self, driver, logged_user):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.wait_main_page_loaded()
        main_page.click_feed()     
        feed_page.wait_feed_page_loaded()

        before_total = feed_page.get_total_orders()

        feed_page.click_constructor()

        main_page.make_burger(INGREDIENTS)

        main_page.click_order_button()
        main_page.wait_order_number_current_loaded()
        main_page.click_close_button_order()
        main_page.wait_order_modal_closed()
        
        main_page.click_feed()

        after_total = feed_page.get_total_orders()
 
        assert after_total == before_total +1

    @allure.title("Проверка увелечения счетчика Выполнено за сегодня")    
    def test_day_orders_counter_increases(self, driver, logged_user):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.wait_main_page_loaded()
        main_page.click_feed()     
        feed_page.wait_feed_page_loaded()

        before_total = feed_page.get_day_orders()

        feed_page.click_constructor()

        main_page.make_burger(INGREDIENTS)

        main_page.click_order_button()
        main_page.wait_order_number_current_loaded()
        main_page.click_close_button_order()
        main_page.wait_order_modal_closed()
        
        main_page.click_feed()

        after_total = feed_page.get_day_orders()
 
        assert after_total == before_total +1


    @allure.title("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_number_in_work(self, driver, logged_user):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.make_burger(INGREDIENTS)

        main_page.click_order_button()
        main_page.wait_order_number_current_loaded()

        order_number = main_page.get_order_number()
        
        main_page.click_close_button_order()
        main_page.wait_order_modal_closed()

        main_page.click_feed()
        feed_page.wait_feed_page_loaded()
        
        feed_page.wait_in_work_current_loaded()
        current_in_work_order = feed_page.get_in_work_order()

        assert current_in_work_order == order_number

import allure

from data.data import INGREDIENTS
from locators.feed_page_locators import FeedPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestOrdersCounter:

    @allure.title("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_number_in_work(self, driver, logged_user):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        # 1. Собрать заказ
        main_page.make_burger(INGREDIENTS)

        # 2. Оформить заказ
        main_page.click_order_button()
        main_page.wait_order_number_current_loaded()

        # 3. Запомнить номер заказа
        order_number = main_page.get_order_number()
        
        # 4. Закрыть окно заказа
        main_page.click_close_button_order()
        main_page.wait_order_modal_closed()

        # 5. Перейти в ленту заказов
        main_page.click_feed()
        feed_page.is_feed_page_open()
        
        # 6. Проверить, что номер появился в блоке "В работе"
        feed_page.wait_in_work_current_loaded()
        current_in_work_order = feed_page.get_in_work_order()

        print(f"Номер который отобразился в разделе в работе: '{current_in_work_order}'")
        print(f"Нормализованный номер из содалки: '{order_number}'")

        assert current_in_work_order == order_number

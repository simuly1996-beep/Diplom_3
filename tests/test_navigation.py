import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestNavigation:

    @allure.title("Проверка перехода на ленту заказов после нажатия на кнопку лента заказов")
    def test_click_feed_go_to_feed_page(self, driver: WebDriver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open_main_page()
        main_page.wait_main_page_loaded()
        main_page.click_feed()

        assert feed_page.is_feed_page_url()

    @allure.title("Проверка перехода на главную страницу  после нажатия на конструктор")
    def test_click_constructor_go_to_main_page(self, driver: WebDriver):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        feed_page.open_feed_page()
        feed_page.wait_feed_page_loaded()
        feed_page.click_constructor()

        assert main_page.is_main_page_url()
import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

from data.data import INGREDIENT_COUNTER_TEST_DATA
from pages.main_page import MainPage

      
class TestIngredientWindow:

    @allure.title("Проверка открытия всплывающего окна детали ингредиента")
    def test_open_ingredient_window(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_main_page_loaded()
        main_page.click_first_bun()

        assert main_page.display_ingredient_details_title()

    @allure.title("Проверка закрытия всплывающего окна детали ингредиента")
    def test_close_ingredient_window(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_main_page_loaded()
        main_page.click_first_bun()

        main_page.click_close_button()

        assert main_page.is_ingredient_window_closed()

class TestIngredientСounter:  

    @pytest.mark.parametrize("counter_locator, ingredient_locator, expected_count", INGREDIENT_COUNTER_TEST_DATA)
    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter_increases(
        self,
        driver: WebDriver,
        counter_locator,
        ingredient_locator,
        expected_count
    ):
        main = MainPage(driver)

        main.open_main_page()
        main.wait_main_page_loaded()

        before = main.get_first_ingredient_counter(counter_locator)

        main.drag_and_drop_first_ingredient(ingredient_locator)
        main.wait_ingredient_counter_updated(counter_locator, str(expected_count))

        after = main.get_first_ingredient_counter(counter_locator)

        assert after == before + expected_count

import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator))
    
    @allure.step("Найти несколько элементов")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Прокрутить до элемента")
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Дождаться видимости элемента")
    def wait_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator))
    
    @allure.step("Дождаться, когда элемент станет кликабельным")    
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Переключиться на новую вкладку")   
    def switch_to_new_tab(self):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
    
    @allure.step("Дождаться, что URL содержит '{text}'")
    def wait_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    @allure.step("Проверка отсутствия видимости элемента")
    def is_not_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться текста '{text}'")
    def wait_text_in_element(self, locator, text):
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        """
        Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
        :param source_locator: Локатор элемента, который нужно перетащить.
        :param target_locator: Локатор элемента, куда нужно перетащить.
        """
        self.find(source_locator)
        self.find(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step("Дождаться исчезновения перекрытия")   
    def wait_overlay_disappear(self, locator):
        self.wait.until(
            lambda d: len(d.find_elements(*locator)) == 0
            or all(
                not e.is_displayed()
                for e in d.find_elements(*locator)
            )
        )

    @allure.step("Ввести текст")
    def send_keys_in_field(self, locator, text):
        element = self.wait_visibility(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить адрес текущей страницы")
    def get_current_url(self):
        return self.driver.current_url
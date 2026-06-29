from selenium.webdriver.common.by import By

class FeedPageLocators:
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")

    # Кнопка Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")

    # заголовок ленты заказа
    FEED_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

    OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")

    # Кнопка Личный Кабинет
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")

    # Счетчика выполнено за все время
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за все время:')]/following-sibling::p")

    DAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]/following-sibling::p")

    ORDER_IN_PROGRESS_BLOCK = (By.XPATH, "//*[text()='В работе']/ancestor::section")

    ORDER_ITEMS = (By.XPATH, "//*[text()='В работе']/following::ul[1]//li")

    ORDER_ITEMS_IN_WORK = (By.XPATH, "//p[normalize-space()='В работе:']/following-sibling::ul[2]/li")
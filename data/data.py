from locators.main_page_locators import MainPageLocators

INGREDIENT_COUNTER_TEST_DATA = [
    (MainPageLocators.FIRST_BUN_COUNTER, MainPageLocators.FIRST_BUN, 2),
    (MainPageLocators.FIRST_SAUCE_COUNTER, MainPageLocators.FIRST_SAUCE, 1),
    (MainPageLocators.FIRST_FILLING_COUNTER, MainPageLocators.FIRST_FILLING, 1),
]

INGREDIENTS = [
    MainPageLocators.FIRST_BUN,
    MainPageLocators.FIRST_SAUCE,
    MainPageLocators.FIRST_FILLING,
]

USER = {
        "email": "test_user1001@gmail.com",
        "password": "123456789",
        "name": "test_user"
    }
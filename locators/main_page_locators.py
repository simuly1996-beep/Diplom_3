from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")

    # Кнопка Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")

    # Первая булка
    FIRST_BUN = (By.XPATH,"(//h2[text()='Булки']/following::a[contains(@class,'BurgerIngredient')])[1]")

    # счетчик первой булки
    FIRST_BUN_COUNTER = (By.XPATH, "(//h2[text()='Булки']/following::a[contains(@class,'BurgerIngredient')])[1]//p[contains(@class,'counter_counter__num')]")

    # Первый соус
    FIRST_SAUCE = (By.XPATH, "(//h2[text()='Соусы']/following::a[contains(@class,'BurgerIngredient')])[1]")

    # счетчик первого соуса
    FIRST_SAUCE_COUNTER = (By.XPATH, "(//h2[text()='Соусы']/following::a[contains(@class,'BurgerIngredient')])[1]//p[contains(@class,'counter_counter__num')]")

    # Первая начинка
    FIRST_FILLING = (By.XPATH, "(//h2[text()='Начинки']/following::a[contains(@class,'BurgerIngredient')])[1]")

    # счетчик первой начинки
    FIRST_FILLING_COUNTER = (By.XPATH, "(//h2[text()='Начинки']/following::a[contains(@class,'BurgerIngredient')])[1]//p[contains(@class,'counter_counter__num')]")


    # заголовок конструтора
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    # заголовок Детали ингредиента в окне карточки ингредиента 
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # кнопка закрытия окна деталей ингредиента
    MODAL_CLOSE_BUTTON = (By.XPATH,"//section[contains(@class,'Modal_modal_opened')]//button")

   
    # область конструктора бургера
    CONSTRUCTOR_AREA = (By.XPATH, "//span[contains(@class, 'BurgerConstructor_basket__listContainer')]")

    OVERLAY = (By.CSS_SELECTOR, "[class*='modal_overlay'][class*='active']")

    # Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH,  "//button[contains(text(),'Оформить заказ')]")

    ORDER_NUMBER = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]/preceding-sibling::h2")
    
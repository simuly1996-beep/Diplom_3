# Stellar Burgers UI Tests

Автоматизированные UI-тесты для веб-приложения **Stellar Burgers**, реализованные с использованием паттерна **Page Object Model (POM)**, запускаемые в **Google Chrome** и **Mozilla Firefox**, с формированием отчётов через **Allure**.

## 📌 Описание проекта

Проект проверяет основную функциональность веб-приложения:

### 🍔 Основной функционал
- переход в раздел **«Конструктор»**
- переход в раздел **«Лента заказов»**
- открытие модального окна с ингредиентом
- закрытие модального окна
- увеличение счётчика ингредиента при добавлении в заказ

### 📊 Раздел «Лента заказов»
- увеличение счётчика **«Выполнено за всё время»**
- увеличение счётчика **«Выполнено за сегодня»**
- появление номера нового заказа в разделе **«В работе»**

## 🧪 Технологии

- Python 3.10+
- pytest
- Selenium WebDriver
- Allure pytest
- Page Object Model (POM)
- Google Chrome / Mozilla Firefox

## 📁 Структура проекта
│
├── data/ # Тестовые данные
│ └── data.py
│
├── locators/ # Локаторы страниц
│ ├── feed_page_locators.py
│ ├── login_page_locators.py
│ ├── main_page_locators.py
│ └── order_page_locators.py
│
├── pages/ # Page Object модели
│ ├── base_page.py
│ ├── feed_page.py
│ ├── login_page.py
│ └── main_page.py
│
├── tests/ # UI тесты
│ ├── test_ingredient_functionality.py
│ ├── test_navigation.py
│ └── test_order_counters.py
│
├── conftest.py # Фикстуры (драйверы Chrome/Firefox и др.)
├── urls.py # URL приложения
└── README.md

---

## Установка
Клонируй репозиторий:

```bash
git clone <URL_репозитория>
cd DIPLOM_3
---

## Установка зависимостей
pip install -r requirements.txt

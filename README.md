# Проект автоматизации тестирования Кинопоиска

## Описание проекта

Проект содержит набор автотестов для проверки функциональности поиска на сайте Кинопоиска. Реализованы как UI-тесты с использованием Selenium WebDriver, так и API-тесты для проверки эндпоинтов поиска фильмов.

**Задача:** автоматизировать проверку поиска фильмов по различным критериям (страна, актёр, год, жанр) как через веб-интерфейс, так и через API.

## Структура проекта

```plaintext
kinopoisk-autotests/
├── test/
│   ├── test_ui.py          # UI-тесты (Selenium)
│   └── test_api.py         # API-тесты (requests)
├── page/
│   ├── __init__.py
│   ├── MainPage.py         # Page Object для главной страницы
│   └── KinopoiskApi.py     # Клиент для работы с API
├── config/
│   ├── __init__.py
│   └── settings.py         # Настройки проекта (URL, версии API)
├── .env                    # Переменные окружения (не в git)
├── .env.example            # Шаблон для .env
├── conftest.py             # Фикстуры pytest
├── pytest.ini              # Настройки pytest
├── requirements.txt        # Зависимости проекта
└── README.md               # Документация
```

## Установка и настройка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/sergood1602/kinopoisk-autotests.git
cd kinopoisk-autotests
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настроить переменные окружения

Создайте файл `.env` в корне проекта и добавьте ваш API-ключ:

```env
KINOPOISK_API_KEY=ваш_реальный_ключ_здесь
```

Пример содержимого можно посмотреть в файле `.env.example`.

## Запуск тестов

### Запуск всех тестов

```bash
pytest -v -s
```

### Запуск только UI-тестов

```bash
pytest -m ui -v -s
```

### Запуск только API-тестов

```bash
pytest -m api -v -s
```

## Запуск с Allure-отчётом

```bash
# Запуск тестов с сохранением результатов
pytest --alluredir=allure-results -v -s

# Генерация отчёта
allure generate allure-results -o allure-report --clean

# Открытие отчёта
allure open allure-report
```

## Содержание тестов

### UI-тесты (`test_ui.py`)

| № | Тест | Описание |
|---|------|----------|
| 1 | `test_search_by_country_and_actor` | Поиск фильмов США с Брэдом Питтом (позитивный) |
| 2 | `test_search_ussr_1994_not_found` | Поиск СССР + 1994 → ничего не найдено |
| 3 | `test_search_invalid_year_202_not_found` | Поиск с невалидным годом "202" → ничего не найдено |
| 4 | `test_search_russia_thriller_brad_pitt_not_found` | Россия + триллер + Брэд Питт → ничего не найдено |
| 5 | `test_search_usa_1961_tom_cruise_not_found` | США + 1961 + Том Круз → ничего не найдено |

### API-тесты (`test_api.py`)

| № | Тест | Описание |
|---|------|----------|
| 1 | `test_search_movies_usa_2010_drama` | Поиск по параметрам (США, 2010, драма) |
| 2 | `test_search_movie_by_query_the_game` | Поиск по названию "The Game" |
| 3 | `test_search_movie_without_token` | Поиск без API-ключа → 401 |
| 4 | `test_search_movies_country_usa_latin` | Поиск по стране "USA" (латиница) → пустой результат |
| 5 | `test_search_movie_invalid_query_syntax` | Невалидный синтаксис запроса → 400 |

## Технологии

- **Python** — язык программирования
- **pytest** — фреймворк для тестирования
- **Selenium WebDriver** — для UI-тестов
- **Requests** — для API-тестов
- **Allure** — для генерации отчётов
- **python-dotenv** — для управления переменными окружения
- **webdriver-manager** — для автоматической установки ChromeDriver

## Требования

- Python 3.8+
- Google Chrome (последняя версия)
- ChromeDriver (устанавливается автоматически через `webdriver-manager`)

## Ссылка на финальный проект

[Ссылка на проект](https://sergood1602-.yonote.ru/share/ecc18fc6-d75e-4b05-bd6a-61c51cd8ac76)

---

**Автор:** Сергей Костромин

**Дата:** 17.06.2026
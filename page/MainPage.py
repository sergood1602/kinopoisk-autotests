# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select

# class MainPage:

#     def __init__(self, driver: WebDriver) -> None:
#         self.__url = "https://www.kinopoisk.ru/"
#         self.__driver = driver

#     def go(self):
#         self.__driver.get(self.__url)
#         search_btn = WebDriverWait(self.__driver, 15).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.styles_advancedSearchIcon__u9ckM")))
#         search_btn.click()


#     def select_country(self, country_name: str):
#         """Выбрать страну из выпадающего списка"""
#         country_select = WebDriverWait(self.__driver, 10).until(
#         EC.presence_of_element_located((By.ID, "country")))
#         select = Select(country_select)
#         select.select_by_visible_text(country_name)

#     def fill_actor(self, actor_name: str):
#         """Заполнить поле 'Актёр'"""
#         actor_field = WebDriverWait(self.__driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='m_act[actor]']")))
#         actor_field.clear()
#         actor_field.send_keys(actor_name)

#     def click_search(self):
#         """Нажать кнопку 'Поиск'"""
#         search_button = WebDriverWait(self.__driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "input.nice_button")))
#         search_button.click()

#     def is_on_search_results_page(self) -> bool:
#         """Проверить, что открыта страница с результатами поиска"""
#         current_url = self.__driver.current_url
#         # Если URL содержит признаки страницы результатов
#         return "search" in current_url.lower() or current_url != self.__url

#     def fill_year(self, year: str):
#         """Заполнить поле 'Год'"""
#         year_field = WebDriverWait(self.__driver, 10).until(
#             EC.presence_of_element_located((By.ID, "year")))
#         year_field.clear()
#         year_field.send_keys(year)

#     def get_not_found_message(self) -> str:
#         """Получить текст сообщения 'ничего не найдено'"""
#         message = WebDriverWait(self.__driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "h2.textorangebig")))
#         return message.text

#     def is_not_found_message_displayed(self) -> bool:
#         """Проверить, отобразилось ли сообщение о том, что ничего не найдено"""
#         try:
#             WebDriverWait(self.__driver, 5).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "h2.textorangebig")))
#             return True
#         except:
#             return False

#     def select_genre(self, genre_name: str):
#         """Выбрать жанр по видимому тексту (например, 'триллер')"""
#         genre_select = WebDriverWait(self.__driver, 10).until(
#             EC.presence_of_element_located((By.ID, "m_act[genre]")))
#         select = Select(genre_select)
#         select.select_by_visible_text(genre_name)

"""
Модуль для работы с главной страницей Кинопоиска и страницей расширенного поиска.

Содержит класс MainPage с методами для взаимодействия с формой поиска фильмов.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import allure
from config.settings import UI_URL


class MainPage:
    """
    Page Object для главной страницы Кинопоиска (https://www.kinopoisk.ru/)
    и страницы расширенного поиска.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        Args:
            driver: WebDriver - экземпляр драйвера Selenium
        """
        self.__url = UI_URL
        self.__driver = driver

    def go(self):
        """
        Открыть главную страницу и перейти в расширенный поиск.

        Returns:
            None

        Raises:
            TimeoutException: Если кнопка расширенного поиска не появилась за 15 секунд
        """
        with allure.step("Открыть главную страницу Кинопоиска"):
            self.__driver.get(self.__url)

        with allure.step("Нажать кнопку расширенного поиска"):
            search_btn = WebDriverWait(self.__driver, 15).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "svg.styles_advancedSearchIcon__u9ckM")
                )
            )
            search_btn.click()

    def select_country(self, country_name: str):
        """
        Выбрать страну из выпадающего списка.

        Args:
            country_name: str - название страны для выбора (например, "США", "Россия", "СССР")

        Returns:
            None

        Raises:
            TimeoutException: Если поле страны не появилось за 10 секунд
            NoSuchElementException: Если указанная страна не найдена в списке
        """
        with allure.step(f"Выбрать страну '{country_name}'"):
            country_select = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.ID, "country"))
            )
            select = Select(country_select)
            select.select_by_visible_text(country_name)

    def fill_actor(self, actor_name: str):
        """
        Заполнить поле 'Актёр'.

        Args:
            actor_name: str - имя актёра (например, "Брэд Питт", "Том Круз")

        Returns:
            None

        Raises:
            TimeoutException: Если поле 'Актёр' не появилось за 10 секунд
        """
        with allure.step(f"Ввести имя актёра '{actor_name}'"):
            actor_field = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[name='m_act[actor]']")
                )
            )
            actor_field.clear()
            actor_field.send_keys(actor_name)

    def click_search(self):
        """
        Нажать кнопку 'Поиск' для выполнения поискового запроса.

        Returns:
            None

        Raises:
            TimeoutException: Если кнопка 'Поиск' не стала кликабельной за 10 секунд
        """
        with allure.step("Нажать кнопку 'Поиск'"):
            search_button = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input.nice_button")
                )
            )
            search_button.click()

    def is_on_search_results_page(self) -> bool:
        """
        Проверить, что открыта страница с результатами поиска.

        Returns:
            bool: True - если URL содержит 'search' или отличается от главной страницы,
                  False - в противном случае
        """
        with allure.step(
            "Проверить, что открыта страница с результатами поиска"
        ):
            current_url = self.__driver.current_url
            is_search_page = (
                "search" in current_url.lower() or current_url != self.__url
            )
            allure.attach(
                current_url, "Текущий URL", allure.attachment_type.TEXT
            )
            return is_search_page

    def fill_year(self, year: str):
        """
        Заполнить поле 'Год'.

        Args:
            year: str - год (например, "1994", "1961" или невалидный "202")

        Returns:
            None

        Raises:
            TimeoutException: Если поле 'Год' не появилось за 10 секунд
        """
        with allure.step(f"Ввести год '{year}'"):
            year_field = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.ID, "year"))
            )
            year_field.clear()
            year_field.send_keys(year)

    def get_not_found_message(self) -> str:
        """
        Получить текст сообщения 'ничего не найдено'.

        Returns:
            str: Текст сообщения (например, "К сожалению, по вашему запросу ничего не найдено...")

        Raises:
            TimeoutException: Если сообщение не появилось за 10 секунд
        """
        with allure.step("Получить текст сообщения 'ничего не найдено'"):
            message = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "h2.textorangebig")
                )
            )
            text = message.text
            allure.attach(text, "Текст сообщения", allure.attachment_type.TEXT)
            return text

    def is_not_found_message_displayed(self) -> bool:
        """
        Проверить, отобразилось ли сообщение о том, что ничего не найдено.

        Returns:
            bool: True - если сообщение отобразилось за 5 секунд,
                  False - если сообщение не появилось
        """
        with allure.step(
            "Проверить отображение сообщения 'ничего не найдено'"
        ):
            try:
                WebDriverWait(self.__driver, 5).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "h2.textorangebig")
                    )
                )
                allure.attach(
                    "Сообщение отобразилось",
                    "Результат",
                    allure.attachment_type.TEXT,
                )
                return True
            except:
                allure.attach(
                    "Сообщение не отобразилось",
                    "Результат",
                    allure.attachment_type.TEXT,
                )
                return False

    def select_genre(self, genre_name: str):
        """
        Выбрать жанр по видимому тексту (например, 'триллер').

        Args:
            genre_name: str - название жанра (например, "триллер", "комедия", "боевик")

        Returns:
            None

        Raises:
            TimeoutException: Если поле 'Жанр' не появилось за 10 секунд
            NoSuchElementException: Если указанный жанр не найден в списке
        """
        with allure.step(f"Выбрать жанр '{genre_name}'"):
            genre_select = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.ID, "m_act[genre]"))
            )
            select = Select(genre_select)
            select.select_by_visible_text(genre_name)

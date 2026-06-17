"""
Класс для работы с API Кинопоиска
"""

import os
import requests
import allure
from dotenv import load_dotenv
from config.settings import API_BASE_URL, API_VERSION_V1_4, API_VERSION_V1_5

# Загружаем переменные из .env
load_dotenv()

KINOPOISK_API_KEY = os.getenv("KINOPOISK_API_KEY")

if not KINOPOISK_API_KEY:
    raise ValueError("KINOPOISK_API_KEY не найден в .env файле")


class KinopoiskApi:
    """Клиент для взаимодействия с API Кинопоиска"""

    def __init__(self):
        self.headers = {
            "X-API-KEY": KINOPOISK_API_KEY,
            "Content-Type": "application/json",
        }

    def search_movies(
        self, year: str = None, country: str = None, genre: str = None
    ) -> dict:
        """
        Поиск фильмов по параметрам (использует API v1.5).

        Args:
            year: str - год выпуска фильма (например, "2010")
            country: str - страна производства (например, "США")
            genre: str - жанр фильма (например, "драма")

        Returns:
            dict: JSON-ответ от API
        """
        with allure.step(
            f"Выполнить API-запрос: year={year}, "
            f"country={country}, genre={genre}"
        ):
            base_url = f"{API_BASE_URL}{API_VERSION_V1_5}"
            url = f"{base_url}/movie"

            params = {}
            if year:
                params["year"] = year
            if country:
                params["countries.name"] = country
            if genre:
                params["genres.name"] = genre

            response = requests.get(url, headers=self.headers, params=params)

            allure.attach(
                f"URL: {response.request.url}",
                "Запрос",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                str(response.status_code),
                "Статус-код",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                response.text[:500],
                "Ответ (первые 500 символов)",
                allure.attachment_type.JSON,
            )

            return response

    def search_by_query(self, query: str) -> dict:
        """
        Поиск фильмов по текстовому запросу (название), использует API v1.4.

        Args:
            query: str - текст для поиска (например, "The Game")

        Returns:
            dict: JSON-ответ от API
        """
        with allure.step(f"Выполнить поиск по запросу '{query}'"):
            base_url = f"{API_BASE_URL}{API_VERSION_V1_4}"
            url = f"{base_url}/movie/search"

            params = {"query": query}

            response = requests.get(url, headers=self.headers, params=params)

            allure.attach(
                f"URL: {response.request.url}",
                "Запрос",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                str(response.status_code),
                "Статус-код",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                response.text[:500],
                "Ответ (первые 500 символов)",
                allure.attachment_type.JSON,
            )

            return response

    def search_by_query_no_token(self, query: str) -> requests.Response:
        """
        Поиск фильмов по текстовому запросу (название) БЕЗ API-ключа.
        Используется для проверки ошибки авторизации.

        Args:
            query: str - текст для поиска (например, "The Game")

        Returns:
            requests.Response: объект ответа от API
        """
        with allure.step(
            f"Выполнить поиск по запросу '{query}' без API-ключа"
        ):
            base_url = f"{API_BASE_URL}{API_VERSION_V1_4}"
            url = f"{base_url}/movie/search"

            params = {"query": query}

            # Отправляем запрос БЕЗ заголовка X-API-KEY
            response = requests.get(url, params=params)

            allure.attach(
                f"URL: {response.request.url}",
                "Запрос",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                str(response.status_code),
                "Статус-код",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                response.text[:500],
                "Ответ (первые 500 символов)",
                allure.attachment_type.TEXT,
            )

            return response

    def search_by_query_invalid(self, query: str) -> requests.Response:
        """
        Поиск фильмов с НЕВАЛИДНЫМ запросом (пропущен знак ?).

        Args:
            query: str - текст для поиска (например, "The Game")

        Returns:
            requests.Response: объект ответа от API
        """
        with allure.step(f"Выполнить невалидный поиск по запросу '{query}'"):
            base_url = f"{API_BASE_URL}{API_VERSION_V1_4}"
            # Намеренно неправильный URL: пропущен знак "?"
            url = f"{base_url}/movie/searchquery={query}"

            response = requests.get(url, headers=self.headers)

            allure.attach(
                f"URL: {response.request.url}",
                "Запрос",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                str(response.status_code),
                "Статус-код",
                allure.attachment_type.TEXT,
            )
            allure.attach(
                response.text[:500],
                "Ответ (первые 500 символов)",
                allure.attachment_type.TEXT,
            )

            return response

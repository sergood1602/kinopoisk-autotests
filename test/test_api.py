"""
API-тесты для проверки поиска фильмов на Кинопоиске
"""

import allure
import pytest
from page.KinopoiskApi import KinopoiskApi


@pytest.mark.api
class TestKinopoiskApi:
    """Класс с API-тестами Кинопоиска"""

    @allure.feature("API поиск фильмов")
    @allure.story("Поиск по параметрам")
    @allure.title("Поиск фильмов США 2010 года в жанре драма")
    @allure.description(
        "Проверяет, что API возвращает статус 200 "
        "и фильмы соответствуют критериям"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("API", "search", "positive")
    def test_search_movies_usa_2010_drama(self):
        """
        Тест: поиск фильмов по году, стране и жанру.

        Параметры:
            - year: 2010
            - country: США
            - genre: драма

        Ожидаемый результат:
            - Статус-код 200
            - Ответ содержит список фильмов
        """
        # Arrange
        api = KinopoiskApi()

        # Act
        response = api.search_movies(
            year="2010",
            country="США",
            genre="драма"
        )

        # Assert
        with allure.step("Проверить статус-код ответа"):
            assert response.status_code == 200, (
                f"Ожидался статус 200, получен {response.status_code}"
            )

        with allure.step("Проверить, что ответ содержит данные"):
            data = response.json()
            assert data is not None, "Ответ не содержит данных"

        with allure.step(
            "Проверить, что в ответе есть поле docs (список фильмов)"
        ):
            assert "docs" in data, "В ответе отсутствует поле 'docs'"
            assert isinstance(data["docs"], list), (
                "Поле 'docs' не является списком"
            )

        with allure.step("Проверить, что найден хотя бы один фильм"):
            assert len(data["docs"]) > 0, "Список фильмов пуст"

    @allure.feature("API поиск фильмов")
    @allure.story("Поиск по названию")
    @allure.title("Поиск фильмов по названию 'The Game'")
    @allure.description(
        "Проверяет, что API возвращает статус 200 "
        "и находит фильм 'The Game'"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("API", "search", "by_query")
    def test_search_movie_by_query_the_game(self):
        """
        Тест: поиск фильма по названию.

        Параметры:
            - query: The Game

        Ожидаемый результат:
            - Статус-код 200
            - Список фильмов содержит 'The Game'
        """
        # Arrange
        api = KinopoiskApi()

        # Act
        response = api.search_by_query(query="The Game")

        # Assert
        with allure.step("Проверить статус-код ответа"):
            assert response.status_code == 200, (
                f"Ожидался статус 200, получен {response.status_code}"
            )

        with allure.step("Проверить, что ответ содержит данные"):
            assert response.text, "Ответ пустой"
            data = response.json()

        with allure.step(
            "Проверить, что среди результатов есть фильм 'The Game'"
        ):
            found = False
            for movie in data["docs"]:
                movie_name = movie.get("name", "")
                if "The Game" in movie_name or "Игра" in movie_name:
                    found = True
                    allure.attach(
                        f"Найден фильм: {movie_name} "
                        f"(ID: {movie.get('id', 'N/A')})",
                        "Результат",
                        allure.attachment_type.TEXT,
                    )
                    break

            assert found, (
                "Фильм 'The Game' не найден в результатах поиска"
            )

    @allure.feature("API поиск фильмов")
    @allure.story("Негативные сценарии")
    @allure.title("Поиск фильма без API-ключа")
    @allure.description(
        "Проверяет, что запрос без токена возвращает статус 401 "
        "(Unauthorized)"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("API", "negative", "unauthorized")
    def test_search_movie_without_token(self):
        """
        Тест: поиск фильма без API-ключа.

        Ожидаемый результат:
            - Статус-код 401 (Unauthorized)
        """
        # Arrange
        api = KinopoiskApi()

        # Act
        response = api.search_by_query_no_token(query="The Game")

        # Assert
        with allure.step("Проверить статус-код ответа"):
            assert response.status_code == 401, (
                f"Ожидался статус 401, получен {response.status_code}"
            )

    @allure.feature("API поиск фильмов")
    @allure.story("Негативные сценарии")
    @allure.title("Поиск фильмов по стране на латинице (USA)")
    @allure.description(
        "Проверяет, что поиск с названием страны на латинице 'USA' "
        "не даёт результатов"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("API", "negative", "invalid_input")
    def test_search_movies_country_usa_latin(self):
        """
        Тест: поиск фильмов по стране, указанной латиницей.

        Параметры:
            - country: USA (вместо США)

        Ожидаемый результат:
            - Статус-код 200
            - Список фильмов пуст (docs = [])
        """
        # Arrange
        api = KinopoiskApi()

        # Act
        response = api.search_movies(country="USA")

        # Assert
        with allure.step("Проверить статус-код ответа"):
            assert response.status_code == 200, (
                f"Ожидался статус 200, получен {response.status_code}"
            )

        with allure.step("Проверить, что ответ содержит поле docs"):
            data = response.json()
            assert "docs" in data, "В ответе отсутствует поле 'docs'"

        with allure.step("Проверить, что список фильмов пуст"):
            assert len(data["docs"]) == 0, (
                f"Ожидался пустой список, "
                f"получено {len(data['docs'])} фильмов"
            )

    @allure.feature("API поиск фильмов")
    @allure.story("Негативные сценарии")
    @allure.title("Поиск с невалидным query-запросом")
    @allure.description(
        "Проверяет, что запрос с неправильным синтаксисом "
        "(пропущен ?) возвращает ошибку 400"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("API", "negative", "invalid_syntax")
    def test_search_movie_invalid_query_syntax(self):
        """
        Тест: поиск с невалидным query-запросом.

        Параметры:
            - Неправильный URL: /movie/searchquery=The Game
              (вместо /movie/search?query=The Game)

        Ожидаемый результат:
            - Статус-код 400 (Bad Request)
        """
        # Arrange
        api = KinopoiskApi()

        # Act
        response = api.search_by_query_invalid(query="The Game")

        # Assert
        with allure.step("Проверить статус-код ответа"):
            assert response.status_code == 400, (
                f"Ожидался статус 400, получен {response.status_code}"
            )

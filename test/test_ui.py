"""
UI-тесты для проверки поиска на Кинопоиске.
"""

import allure
import pytest
from page.MainPage import MainPage


@pytest.mark.ui
class TestKinopoiskSearch:
    """Класс с тестами для страницы расширенного поиска Кинопоиска"""

    @allure.feature("Поиск фильмов")
    @allure.story("Позитивные сценарии")
    @allure.title("Поиск фильмов США с актёром Брэд Питт")
    @allure.description(
        "Проверяет, что поиск по стране 'США' и актёру 'Брэд Питт' "
        "возвращает страницу с результатами"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "positive", "search")
    def test_search_by_country_and_actor(self, browser):
        """Тест: поиск по стране и актёру."""
        with allure.step("Инициализировать главную страницу"):
            page = MainPage(browser)

        page.go()

        with allure.step("Выбрать страну 'США'"):
            page.select_country("США")

        with allure.step("Ввести актёра 'Брэд Питт'"):
            page.fill_actor("Брэд Питт")

        page.click_search()

        with allure.step("Проверить, что открылась страница с результатами"):
            assert page.is_on_search_results_page(), (
                "Страница с результатами поиска не открылась"
            )

    @allure.feature("Поиск фильмов")
    @allure.story("Негативные сценарии")
    @allure.title("Поиск фильмов СССР 1994 года")
    @allure.description(
        "Проверяет, что поиск по стране 'СССР' и году '1994' "
        "возвращает сообщение 'ничего не найдено'"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "negative", "no_results")
    def test_search_ussr_1994_not_found(self, browser):
        """Тест: поиск по стране и году без результатов."""
        with allure.step("Инициализировать главную страницу"):
            page = MainPage(browser)

        page.go()

        with allure.step("Выбрать страну 'СССР'"):
            page.select_country("СССР")

        with allure.step("Ввести год '1994'"):
            page.fill_year("1994")

        page.click_search()

        with allure.step(
            "Проверить отображение сообщения 'ничего не найдено'"
        ):
            assert page.is_not_found_message_displayed(), (
                "Сообщение 'ничего не найдено' не отобразилось"
            )

    @allure.feature("Поиск фильмов")
    @allure.story("Негативные сценарии")
    @allure.title("Поиск с невалидным форматом года")
    @allure.description(
        "Проверяет, что поиск с годом '202' (неполный формат) "
        "возвращает сообщение 'ничего не найдено'"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "negative", "boundary", "invalid_input")
    def test_search_invalid_year_202_not_found(self, browser):
        """Тест: поиск с невалидным годом."""
        with allure.step("Инициализировать главную страницу"):
            page = MainPage(browser)

        page.go()

        with allure.step("Ввести невалидный год '202'"):
            page.fill_year("202")

        page.click_search()

        with allure.step(
            "Проверить отображение сообщения 'ничего не найдено'"
        ):
            assert page.is_not_found_message_displayed(), (
                "Сообщение 'ничего не найдено' не отобразилось"
            )

    @allure.feature("Поиск фильмов")
    @allure.story("Негативные сценарии")
    @allure.title("Поиск российских триллеров с Брэдом Питтом")
    @allure.description(
        "Проверяет, что поиск по стране 'Россия', жанру 'триллер' "
        "и актёру 'Брэд Питт' возвращает сообщение 'ничего не найдено'"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "negative", "multi_criteria")
    def test_search_russia_thriller_brad_pitt_not_found(self, browser):
        """Тест: поиск по стране, жанру и актёру без результатов."""
        with allure.step("Инициализировать главную страницу"):
            page = MainPage(browser)

        page.go()

        with allure.step("Выбрать страну 'Россия'"):
            page.select_country("Россия")

        with allure.step("Выбрать жанр 'триллер'"):
            page.select_genre("триллер")

        with allure.step("Ввести актёра 'Брэд Питт'"):
            page.fill_actor("Брэд Питт")

        page.click_search()

        with allure.step(
            "Проверить отображение сообщения 'ничего не найдено'"
        ):
            assert page.is_not_found_message_displayed(), (
                "Сообщение 'ничего не найдено' не отобразилось"
            )

    @allure.feature("Поиск фильмов")
    @allure.story("Негативные сценарии")
    @allure.title("Поиск фильмов США 1961 года с Томом Крузом")
    @allure.description(
        "Проверяет, что поиск по стране 'США', году '1961' "
        "и актёру 'Том Круз' возвращает сообщение 'ничего не найдено'"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "negative", "no_results")
    def test_search_usa_1961_tom_cruise_not_found(self, browser):
        """Тест: поиск по стране, году и актёру без результатов."""
        with allure.step("Инициализировать главную страницу"):
            page = MainPage(browser)

        page.go()

        with allure.step("Выбрать страну 'США'"):
            page.select_country("США")

        with allure.step("Ввести год '1961'"):
            page.fill_year("1961")

        with allure.step("Ввести актёра 'Том Круз'"):
            page.fill_actor("Том Круз")

        page.click_search()

        with allure.step(
            "Проверить отображение сообщения 'ничего не найдено'"
        ):
            assert page.is_not_found_message_displayed(), (
                "Сообщение 'ничего не найдено' не отобразилось"
            )

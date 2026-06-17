import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    with allure.step("Открыть и настроить браузер Chrome"):
        browser = webdriver.Chrome()
        browser.maximize_window()
        yield browser
        browser.quit()

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    """Вызывает драйвер для управления работой браузера на базе выбранного webdriver.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

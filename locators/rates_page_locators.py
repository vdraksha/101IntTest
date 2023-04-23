from selenium.webdriver.common.by import By


class RatesPageLocators:
    """Хранит локаторы для страницы https://piter-online.net/leningradskaya-oblast/rates
    """
    CLOSE_POPUP = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]")
    CONNECT_BUTTONS = (By.CSS_SELECTOR, "div[class='app421']")

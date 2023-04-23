from selenium.webdriver.common.by import By


class MainPageLocators:
    """Хранит локаторы для страницы https://piter-online.net/
    """
    STREET_INPUT = (By.CSS_SELECTOR, "input[class='app141 app148 app147 app143 app160 app142']")
    HOUSE_INPUT = (By.CSS_SELECTOR, "input[class='app141 app148 app147 app143 app160']")
    TYPE_INPUT = (By.CSS_SELECTOR, "div[class='app164 app167 app201 app165 app199'] li:nth-child(1)")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "div[class='app205 app237 app233 app228 app217 app234']")

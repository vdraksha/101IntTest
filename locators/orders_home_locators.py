from selenium.webdriver.common.by import By


class OrdersHomeLocators:
    """Хранить локаторы для страницы https://piter-online.net/leningradskaya-oblast/orders/home
    """
    INPUT_NAME = (By.CSS_SELECTOR, "input[datatest='providers_provider_order_input_name']")
    INPUT_PHONE = (By.CSS_SELECTOR, "input[datatest='providers_provider_order_input_tel']")
    CONNECT_BUTTON = (By.CSS_SELECTOR, "div[data-test='order_form_input_connect_button']")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(text(),'Ваша заявка на подключение принята в работу.')]")

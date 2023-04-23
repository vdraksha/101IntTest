from selenium.common import TimeoutException

from locators.orders_home_locators import OrdersHomeLocators
from page.base_page import BasePage


class OrdersHomePage(BasePage):
    """Хранить действия для страницы https://piter-online.net/leningradskaya-oblast/orders/home
    """
    locators = OrdersHomeLocators()

    def fill_all_fields(self):
        """Заполняет поля с именем и номером телефона.
        """
        #self.element_is_visible(self.locators.INPUT_NAME).send_keys('Автотест')
        self.element_is_visible(self.locators.INPUT_PHONE).send_keys('1111111111')

    def click_connect_button(self):
        """Нажимает на кнопку отправки имени и номера телефона.
        """
        connect_button = self.element_is_visible(self.locators.CONNECT_BUTTON)
        self.driver.execute_script("arguments[0].click();", connect_button)

    def get_success_text(self):
        """Получает текст, подтверждающий успешность отправки.
        """
        try:
            return self.element_is_visible(self.locators.SUCCESS_TEXT).text
        except TimeoutException:
            return "Текст не появился!"

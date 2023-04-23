import random

from locators.rates_page_locators import RatesPageLocators
from page.base_page import BasePage


class RatesPage(BasePage):
    """Хранит действия для страницы https://piter-online.net/leningradskaya-oblast/rates
    """
    locators = RatesPageLocators()

    def close_popup(self):
        """Закрывает попап, появившийся при загрузке страницы.
        """
        close_popup = self.element_is_visible(self.locators.CLOSE_POPUP)
        self.driver.execute_script("arguments[0].click();", close_popup)

    def click_connect_button(self):
        """Получает список кнопок подключения к тарифам и нажимает на одну, рандомно выбранную.
        """
        connect_buttons_list = self.element_are_visible(self.locators.CONNECT_BUTTONS)
        connect_button = connect_buttons_list[random.randint(0, len(connect_buttons_list)-1)]
        connect_button.click()

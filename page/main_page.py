from selenium.webdriver import Keys

from page.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Хранит действия для страницы https://piter-online.net/
    """
    locators = MainPageLocators()

    def fill_all_fields(self):
        """Заполняет поля: улица, дом, тип подключения.
        """
        street_input = self.element_is_visible(self.locators.STREET_INPUT)
        street_input.send_keys('Тестовая линия')
        street_input.click()
        street_input.send_keys(Keys.ENTER)

        house_input = self.element_is_visible(self.locators.HOUSE_INPUT)
        self.go_to_element(house_input)
        house_input.send_keys('1')
        house_input.send_keys(Keys.ENTER)

        type_input = self.element_is_visible(self.locators.TYPE_INPUT)
        self.go_to_element(house_input)
        type_input.click()

    def click_submit_button(self):
        """Нажимает на кнопку 'Показать тарифы'
        """
        submit_button = self.element_is_visible(self.locators.SUBMIT_BUTTON)
        submit_button.click()

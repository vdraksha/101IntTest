from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Представление базовой страницы и её методов, которые будут наследовать представления
       других страниц для работы с их элементами.
    """

    def __init__(self, driver, url=""):
        """Инициализация переменных для открытия страницы.
           :param driver: Вызывает драйвер. Передавать как driver.
           :param url: Адрес страницы.
        """
        self.driver = driver
        self.url = url

    def open_url(self):
        """Открытие страницы по url
        """
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Ожидает загрузку и отображение одного элемента на странице для взаимодействия с ним.
           :param locator: Указание на место элемента в html-документе(xpath, селектор).
           :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        """Ожидает загрузку и отображение всех элементов на странице для взаимодействия с ними.
           :param locator: Указание на место элементом в html-документе(xpath, селектор).
           :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def go_to_element(self, locator):
        """Перемещает к указанному элементу на странице.
           :param locator: Указание на место элемента в html-документе(xpath, селектор).
        """
        return ActionChains(self.driver).move_to_element(locator).perform()

    def refresh_page(self):
        """Обновляет текущую страницу браузера.
        """
        self.driver.refresh()



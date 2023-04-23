import requests as req

from page.main_page import MainPage
from page.orders_home_page import OrdersHomePage
from page.rates_page import RatesPage


class TestCriticalPath:

    class TestCriticalPath:

        def test_critical_path(self, driver):
            main_page = MainPage(driver, "https://piter-online.net/")
            main_page.open_url()
            main_page.fill_all_fields()
            main_page.click_submit_button()

            rates_page = RatesPage(driver)
            rates_page.close_popup()
            rates_page.click_connect_button()

            orders_home_page = OrdersHomePage(driver)
            count = 3
            while True:
                count -= 1

                orders_home_page.fill_all_fields()
                orders_home_page.click_connect_button()
                success_text = orders_home_page.get_success_text()
                assert success_text == "Ваша заявка на подключение принята в работу.", \
                                       "Не был получен текст подтверждения."

                response = req.post("https://piter-online.net/api/sites/webhook?type=site101-order-home",
                                    {"fio": "",
                                     "phone_connection": "71111111111",
                                     "need_convergent": "",
                                     "convergent_tariff_id": None,
                                     "region_id": None,
                                     "lead_form_type": "",
                                     "convergent_display_price": None,
                                     "convergent_name": "",
                                     "convergent_tv_channels": None,
                                     "convergent_tv_channels_hd": None,
                                     "convergent_sms": "",
                                     "convergent_sms_type": None,
                                     "convergent_internet": "",
                                     "convergent_internet_type": None,
                                     "convergent_calls": "",
                                     "convergent_calls_type": None,
                                     "tariff_id": "",
                                     "ga_client_id": "",
                                     "uuid": ""})
                status = response.status_code
                assert status == 200, "Статус код POST-запроса заявки отличается от 200."

                if count > 0:
                    orders_home_page.refresh_page()
                else:
                    break






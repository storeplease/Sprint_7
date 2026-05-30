import allure
import requests
import data
from helpers import TestHelper

class OrderMethods:
    def __init__(self):
        self.base_url = data.BASE_URL
        self.timeout = 10
        
    @allure.step("Создание заказа")
    def create_order(self, params=None):
        if params is None:
            params = self.generate_order_params()
        response  = requests.post(self.base_url + data.ORDERS_ENDPOINT, json=params, timeout=self.timeout)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Получение списка заказов")
    def get_orders(self, courier_id):
        url = f"{self.base_url}{data.ORDERS_ENDPOINT}?courierId={courier_id}"
        response  = requests.get(url, timeout=self.timeout)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Проверка статуса ответа")
    def check_response(self, response, expected_status_code):
        return response.status_code == expected_status_code

    def generate_order_params(self):
        return {
            "firstName": TestHelper.generate_random_string(),
            "lastName": TestHelper.generate_random_string(),
            "address": TestHelper.generate_random_string(),
            "metroStation": TestHelper.generate_random_string(),
            "phone": TestHelper.generate_random_string(),
            "rentTime": 1,
            "deliveryDate": "2026-02-05",
            "comment": TestHelper.generate_random_string(),
            "color": ["BLACK"]
        }
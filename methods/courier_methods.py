import allure
import requests
import data
from helpers import TestHelper

class CourierMethods:
    def __init__(self):
        self.base_url = data.BASE_URL
        self.timeout = 10

    @allure.step("Создание курьера")
    def create_courier(self, params=None):
        if params is None:
            params = self.generate_courier_params()
        response  = requests.post(self.base_url + data.COURIER_ENDPOINT, json=params, timeout=self.timeout)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code
        
    @allure.step("Авторизация курьера")
    def login_courier(self, params=None):
        if params is None:
            attributes = self.generate_courier_params()
            params = {
                "login": attributes["login"],
                "password": attributes["password"]
            }
        response  = requests.post(self.base_url + data.LOGIN_ENDPOINT, json=params, timeout=self.timeout)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        response  = requests.delete(f"{self.base_url}{data.COURIER_ENDPOINT}/{courier_id}")
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Проверка статуса ответа")
    def check_response(self, response, expected_status_code):
        return response.status_code == expected_status_code

    def generate_courier_params(self):
        return {
            "login": TestHelper.generate_random_string(),
            "password": TestHelper.generate_random_string(),
            "firstName": TestHelper.generate_random_string()
        }
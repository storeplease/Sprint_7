import allure
import pytest
from methods.order_methods import OrderMethods

class TestCreateOrder:
    @allure.title("Тестируем создание заказа")
    @allure.step("Тест успешного создания заказа")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_success(self, color):
        order_methods = OrderMethods()
        params = order_methods.generate_order_params()
        params["color"] = color
        response_data, status_code = order_methods.create_order(params=params)
        assert status_code == 201 and "track" in response_data, f"Expected status code 201, got {status_code} or Response does not contain 'track'"
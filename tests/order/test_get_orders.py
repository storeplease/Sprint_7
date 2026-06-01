import allure
from methods.order_methods import OrderMethods

class TestGetOrders:
    @allure.title("Тестируем получение списка заказов")
    @allure.step("Тест успешного получения списка заказов")
    def test_get_orders_success(self, courier_with_orders):
        courier_id, order_methods = courier_with_orders
        response_data, status_code = order_methods.get_orders(courier_id)
        assert status_code == 200 and isinstance(response_data.get("orders"), list), f"Expected 200 and orders list, got {status_code} and {response_data}"
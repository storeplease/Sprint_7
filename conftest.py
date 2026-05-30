
import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@pytest.fixture()
def courier_new():
    courier_methods = CourierMethods()
    params = courier_methods.generate_courier_params()
    response_data, status_code = courier_methods.create_courier(params)
    login_response, _ = courier_methods.login_courier({
        "login": params["login"],
        "password": params["password"]
    })
    yield response_data, status_code
    # Код для удаления курьера после теста
    courier_methods.delete_courier(courier_id=login_response["id"])

@pytest.fixture()
def courier_login():
    courier_methods = CourierMethods()
    params = courier_methods.generate_courier_params()

    # Создаём курьера
    courier_methods.create_courier(params)

    # Логинимся и отдаём результат логина
    login_response, login_status = courier_methods.login_courier({
        "login": params["login"],
        "password": params["password"]
    })

    yield login_response, login_status

    # Удаляем по id
    courier_methods.delete_courier(courier_id=login_response["id"])

@pytest.fixture()
def courier_with_orders():
    courier_methods = CourierMethods()
    order_methods = OrderMethods()
    params = courier_methods.generate_courier_params()
    courier_methods.create_courier(params)
    login_resp, _ = courier_methods.login_courier({
        "login": params["login"],
        "password": params["password"]
    })
    courier_id = login_resp["id"]
    order_methods.create_order(order_methods.generate_order_params())
    yield courier_id, order_methods
    courier_methods.delete_courier(courier_id=courier_id)
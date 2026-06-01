
import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@pytest.fixture()
def courier_data():
    courier_methods = CourierMethods()
    params = courier_methods.generate_courier_params()
    yield courier_methods, params
    # Очистка: логинимся и удаляем
    login_resp, _ = courier_methods.login_courier({
        "login": params["login"],
        "password": params["password"]
    })
    courier_methods.delete_courier(courier_id=login_resp["id"])

@pytest.fixture()
def registered_courier():
    courier_methods = CourierMethods()
    params = courier_methods.generate_courier_params()

    # Создаём курьера
    courier_methods.create_courier(params)
    
    yield courier_methods, params
    
    login_resp, _ = courier_methods.login_courier({
        "login": params["login"],
        "password": params["password"]
    })
    courier_methods.delete_courier(courier_id=login_resp["id"])

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

@pytest.fixture()
def existing_courier():
    courier_methods = CourierMethods()
    params = courier_methods.generate_courier_params()
    courier_methods.create_courier(params)
    yield courier_methods, params
    login_resp, _ = courier_methods.login_courier({
        "login": params["login"],
        "password": params["password"]
    })
    courier_methods.delete_courier(courier_id=login_resp["id"])
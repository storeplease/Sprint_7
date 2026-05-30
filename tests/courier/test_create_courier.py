import allure
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title("Тестируем регистрацию аккаунта курьера")
    @allure.step("Тест создания нового курьера")
    def test_create_courier_success(self, courier_new):
        courier_data, status_code = courier_new
        assert status_code == 201 and "ok" in courier_data, f"Expected status code 201, got {status_code} or Response does not contain 'ok'"
    
    @allure.step("Тест ошибки создания курьера с теми же данными")
    def test_create_duplicate_courier(self):
        courier_methods = CourierMethods()
        params = courier_methods.generate_courier_params()
        # Создаем курьера с определенными данными
        response_data, status_code = courier_methods.create_courier(params=params)
        # Пытаемся создать курьера с теми же данными
        duplicate_response_data, duplicate_status_code = courier_methods.create_courier(params=params)
        # Логинимся и удаляем первого курьера
        login_response, _ = courier_methods.login_courier({"login": params["login"], "password": params["password"]})
        courier_methods.delete_courier(courier_id=login_response["id"])
        assert duplicate_status_code == 409, f"Expected status code 409 for duplicate courier, got {duplicate_status_code}"

    @allure.step("Тест ошибки создания курьера без обязательного поля")
    def test_create_courier_missing_field(self):
        courier_methods = CourierMethods()
        params = courier_methods.generate_courier_params()
        # Удаляем обязательное поле "password"
        del params["password"]
        response_data, status_code = courier_methods.create_courier(params=params)
        assert status_code == 400, f"Expected status code 400 for missing field, got {status_code}"

import allure
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title("Тестируем регистрацию аккаунта курьера")
    @allure.step("Тест создания нового курьера")
    def test_create_courier_success(self, courier_data):
        courier_methods, params = courier_data
        response_data, status_code = courier_methods.create_courier(params=params)
        assert status_code == 201 and "ok" in response_data, f"Expected status code 201, got {status_code} or Response does not contain 'ok'"

    @allure.step("Тест ошибки создания курьера с теми же данными")
    def test_create_duplicate_courier(self, existing_courier):
        courier_methods, params = existing_courier
        duplicate_response_data, duplicate_status_code = courier_methods.create_courier(params=params)
        assert duplicate_status_code == 409, f"Expected 409, got {duplicate_status_code}"

    @allure.step("Тест ошибки создания курьера без обязательного поля")
    def test_create_courier_missing_field(self):
        courier_methods = CourierMethods()
        params = courier_methods.generate_courier_params()
        # Удаляем обязательное поле "password"
        del params["password"]
        response_data, status_code = courier_methods.create_courier(params=params)
        assert status_code == 400, f"Expected status code 400 for missing field, got {status_code}"

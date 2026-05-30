import allure
from methods.courier_methods import CourierMethods

class TestLoginCourier:
    @allure.title("Тестируем авторизацию курьера")
    @allure.step("Тест успешной авторизации курьера")
    def test_login_courier_success(self, courier_login):
        courier_data, status_code = courier_login
        assert status_code == 200 and "id" in courier_data, f"Expected status code 200, got {status_code} or Response does not contain 'id'"
    
    @allure.step("Тест ошибки авторизации без обязательного поля")
    def test_login_courier_missing_field(self):
        courier_methods = CourierMethods()
        params = courier_methods.generate_courier_params()
        # Удаляем обязательное поле "password"
        del params["login"]
        response_data, status_code = courier_methods.login_courier(params=params)
        assert status_code == 400, f"Expected status code 400 for missing field, got {status_code}"

    @allure.step("Тест ошибки авторизации с неверными данными")
    def test_login_courier_invalid_credentials(self):
        courier_methods = CourierMethods()
        params = {
            "login": "invalid_login",
            "password": "invalid_password"
        }
        response_data, status_code = courier_methods.login_courier(params=params)
        assert status_code == 404, f"Expected 404, got {status_code}"
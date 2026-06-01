
# URL-адреса для API
BASE_URL = 'http://qa-scooter.praktikum-services.ru'
ORDERS_ENDPOINT = '/api/v1/orders'
COURIER_ENDPOINT = '/api/v1/courier'
LOGIN_ENDPOINT = '/api/v1/courier/login'

# Данные для заказа
order_data = [
    {
        "name": "Максим",
        "surname": "Смирнов",
        "address": "Москва, ул. Строителей, д. 7",
        "station": "Черкизовская",
        "phone": "89991112233",
        "date": "01.05.2026",
        "period": "сутки",
        "color": "black",
        "comment": "Позвоните на мобильный, если что-то будет не так"
    },
    {
        "name": "Алексей",
        "surname": "Иванов",
        "address": "Москва, ул. Гоголя, д. 15",
        "station": "Сокольники",
        "phone": "89992223344",
        "date": "02.05.2026",
        "period": "двое суток",
        "color": "grey",
        "comment": "жду смс с кодом от замка"
    }
]
class TestUsers:

    def test_registration_201(self, registration):
        assert registration.status_code == 201
        assert registration.json()["message"] == "Успешная регистрация!"

    def test_registration_status_code_409(self, registration):
        assert registration.status_code == 201, (
            f"Ожидали получить статус код: 201, получили: {registration.status_code}")

    def test_registration_409_message(self, registration):
        assert registration.json()["message"] == "Успешная регистрация!", (
            f"Ожидали получить сообщение: Успешная регистрация! Получили: {registration.json()["message"]}")

    def test_authorization(self, authorization):
        assert authorization.status_code == 200
        assert type(authorization.json()["token"]) == str

    def test_authorization_status_code_401(self, authorization):
        assert authorization.status_code == 200, (
            f"Ожидали получить статус код: 201, получили: {authorization.status_code}")

    def test_authorization_401_message(self, authorization):
        assert type(authorization.json()["token"]) == str, (
            f"Ожидали получить тип данных str по ключу token Получили: {authorization.json()["message"]}")

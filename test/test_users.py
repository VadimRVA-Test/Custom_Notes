class TestUsers:

    def test_registration(self, registration):
        assert registration.json()["message"] == "Успешная регистрация!", (
            f"Ожидали сообщение Успешная регистрация!, получили {registration.json()["message"]}")
        assert registration.status_code == 201, (
            f"Ожидали статус код 201, получили {registration.status_code}")

    def test_authorization(self, authorization):
        assert authorization.status_code == 200, (
            f"Ожидали статус код 200, получили {authorization.status_code}")
        assert type(authorization.json()) == dict, (
            f"Ожидали получить тип данных Словарь!, получили {type(authorization.json())}")

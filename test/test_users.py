from data.json_for_post import data_user
from data.json_for_post import body_note


class TestUsers:

    def test_registration(self, obj_registration):
        email, password, username = data_user["email"], data_user["password"], data_user["username"]
        response = obj_registration.registration_user(email, password, username)
        if response.status_code == 201:
            assert response.status_code == 201
            assert response.json()["message"] == "Успешная регистрация!"
        elif response.status_code == 409:
            assert response.json()["message"] == "Не успешная регистрация!", (
                f"Ожидали статус код: 201, получили: {response.status_code}",
                f"Ожидали получить сообщение: Успешная регистрация! Получили: {response.json()["message"]}")
        else:
            assert response.status_code == 201, (
                f"Ожидали статус код: 201 Получили: {response.status_code}")

    def test_authorization(self, obj_authorization):
        email, password = data_user["email"], data_user["password"]
        response = obj_authorization.authorization_user(email, password)
        if response.status_code == 200:
            assert response.status_code == 200
            assert type(response.json()["token"]) == str
        elif response.status_code == 401:
            assert response.status_code == 200, (
                f"Ожидали получить статус код: 200, получили: {response.status_code}",
                f"Ожидали получить токен авторизации, получили {response.json()["message"]}")
        else:
            assert response.status_code == 200, (
                f"Ожидали статус код: 201 Получили: {response.status_code}")

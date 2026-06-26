from test.data.json_for_post import data_user, data_user2


class TestUsers:

    def test_registration(self, obj_registration):
        response = obj_registration.registration_user(data_user2["email"], data_user["password"], data_user["username"])
        assert response.status_code == 201, f"Ожидали получить статус код: 201, получили: {response.status_code}"
        assert response.json()["message"] == "Успешная регистрация!", (
            f"Ожидали получить сообщение:Успешная регистрация! Получили: {response.json()["message"]}")

    def test_registration_resource_conflict(self, obj_registration):
        response = obj_registration.registration_user(data_user["email"], data_user["password"], data_user["username"])
        assert response.status_code == 409, (
            f"Ожидали получить статус код: 409, получили: {response.status_code}")
        assert response.json()["message"] == "Пользователь с таким email уже существует", (
            f"Ожидали получить сообщение: Пользователь с таким email уже существует "
            f"Получили: {response.json()["message"]}")

    def test_authorization(self, obj_authorization):
        response = obj_authorization.authorization_user(data_user["email"], data_user["password"])
        assert response.status_code == 200, f"Ожидали получить статус код: 200, получили: {response.status_code}"
        assert len(response.json()["token"]) == 125, f"Ожидали получить token получили: {response.json()["message"]}"
        assert type(response.json()["token"]) == str, f"Ожидали получить token получили: {response.json()["message"]}"

    def test_authorization_token_is_empty_l(self, obj_authorization):
        response = obj_authorization.authorization_user("", data_user["password"])
        assert response.status_code == 401, (
            f"Ожидали получить статус код: 401, получили: {response.status_code}")
        assert response.json()["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль", (
            f"Ожидали получить: Ошибка авторизации... Пожалуйста, проверь почту или пароль"
            f"Получили: {response.json()["message"]}")

    def test_authorization_token_is_empty_p(self, obj_authorization):
        response = obj_authorization.authorization_user(data_user["email"], "")
        assert response.status_code == 401, (
            f"Ожидали получить статус код: 401, получили: {response.status_code}")
        assert response.json()["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль", (
            f"Ожидали получить: Ошибка авторизации... Пожалуйста, проверь почту или пароль"
            f"Получили: {response.json()["message"]}")

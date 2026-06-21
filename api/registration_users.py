from api.base_api import BaseApi


class RegistrationUsers(BaseApi):
    ENDPOINT_1 = "api/register"

    def registration_user(self, email, password, username):
        user_data = {"email": email, "password": password, "username": username}
        return self._requests("POST", endpoint=self.ENDPOINT_1, json=user_data)

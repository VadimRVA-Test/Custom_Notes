from api.base_api import BaseApi


class RegistrationUsers(BaseApi):
    ENDPOINT = "api/register"

    def registration_user(self, email, password, username):
        user_data = {"email": email, "password": password, "username": username}
        return self._requests(method="POST", endpoint=self.ENDPOINT, json=user_data)

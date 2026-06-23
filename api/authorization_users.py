from api.base_api import BaseApi


class AuthorizationUsers(BaseApi):
    ENDPOINT = "/api/login"

    def authorization_user(self, email, password):
        user_data = {"email": email, "password": password}
        return self._requests(method="POST", endpoint=self.ENDPOINT, json=user_data)

    def get_token(self, email, password):
        token = self.authorization_user(email, password)
        return token.json()['token']

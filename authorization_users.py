from base_api import BaseApi


class AuthorizationUsers(BaseApi):
    ENDPOINT_2 = "/api/login"

    def authorization_j(self,  email, password):
        user_data = {"email": email, "password": password}
        return self._requests("POST", endpoint=self.ENDPOINT_2, json=user_data)

    def get_token(self, email, password):
        token = self.authorization_j(email, password)
        return token.json()['token']

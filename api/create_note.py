from api.base_api import BaseApi


class CreateNotes(BaseApi):
    def __init__(self, token):
        self.ENDPOINT = "/api/notes"
        self.token = token

    def create_note(self, need_token, note):
        return self._requests(method="POST", endpoint=self.ENDPOINT, need_token=need_token, json=note)

from api.base_api import BaseApi


class CreateNotes(BaseApi):
    def __init__(self, token):
        self.ENDPOINT_3 = "/api/notes"
        self.token = token

    def create_notes(self, note):
        return self._requests("POST", endpoint=self.ENDPOINT_3, need_token=True, json=note)

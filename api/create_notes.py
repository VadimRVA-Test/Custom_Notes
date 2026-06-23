from api.base_api import BaseApi


class CreateNotes(BaseApi):
    def __init__(self, token):
        self.ENDPOINT = "/api/notes"
        self.token = token

    def create_notes_201(self, note):
        return self._requests(method="POST", endpoint=self.ENDPOINT, need_token=True, json=note)

    def create_notes_401(self, note):
        return self._requests(method="POST", endpoint=self.ENDPOINT, need_token=False, json=note)

    def create_notes_403(self, need_token=False, note=None):
        return self._requests(
            method="POST",
            endpoint=self.ENDPOINT,
            need_token=self._false_token(need_token),
            json=note)

    def _false_token(self, need_token=False):
        if need_token:
            self.token = "hg"
            return self.token
        return self.token

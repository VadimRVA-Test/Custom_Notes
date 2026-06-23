from api.base_api import BaseApi


class GetNotes(BaseApi):
    def __init__(self, token):
        self.ENDPOINT = "/api/notes"
        self.token = token

    def get_all_notes_status_code_200(self):
        return self._requests(method="GET", endpoint=self.ENDPOINT, need_token=True)

    def get_all_notes_status_code_401(self):
        return self._requests(method="GET", endpoint=self.ENDPOINT, need_token=False)

    def get_all_notes_status_code_403(self, need_token=True):
        return self._requests(method="GET", endpoint=self.ENDPOINT, need_token=self._false_token2(need_token))

    def get_not_id_by_title(self, title):
        all_notes = self.get_all_notes_status_code_200()
        for note in all_notes.json():
            if note["title"] == title:
                note = note["id"]
                return note
        return None

    def _false_token2(self, need_token=False):
        if need_token:
            self.token = "hg"
            return self.token
        return self.token

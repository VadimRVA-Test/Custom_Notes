from api.base_api import BaseApi


class GetNotes(BaseApi):
    def __init__(self, token):
        self.ENDPOINT = "/api/notes"
        self.token = token

    def get_all_notes(self, need_token):
        return self._requests(method="GET", endpoint=self.ENDPOINT, need_token=need_token)

    def get_not_id_by_title(self, need_token, title):
        all_notes = self.get_all_notes(need_token)
        for note in all_notes.json():
            if note["title"] == title:
                note = note["id"]
                return note
        return None

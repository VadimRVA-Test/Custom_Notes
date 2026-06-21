from api.base_api import BaseApi


class GetNotes(BaseApi):
    def __init__(self, token):
        self.ENDPOINT_3 = "/api/notes"
        self.token = token

    def get_all_notes(self):
        return self._requests("GET", endpoint=self.ENDPOINT_3, need_token=True)

    def get_not_id_by_title(self, title):
        all_notes = self.get_all_notes()
        for note in all_notes.json():
            if note["title"] == title:
                return note["id"]
        return None

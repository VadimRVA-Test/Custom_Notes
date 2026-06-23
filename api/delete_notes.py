from api.base_api import BaseApi


class DeleteNote(BaseApi):
    def __init__(self, token):
        self.ENDPOINT = "/api/notes"
        self.token = token

    def delete_notes_status_code_200(self, id_note):
        return self._requests(method="DELETE", endpoint=self.ENDPOINT, need_token=True, note_id=id_note)

    def delete_notes_status_code_401(self, id_note):
        return self._requests(method="DELETE", endpoint=self.ENDPOINT, need_token=False, note_id=id_note)

    def delete_notes_status_code_403(self, id_note, need_token=True):
        return self._requests(
            method="DELETE",
            endpoint=self.ENDPOINT,
            need_token=self._false_token(need_token),
            note_id=id_note)

    def _false_token(self, need_token=False):
        if need_token:
            self.token = "hg"
            return self.token
        return self.token

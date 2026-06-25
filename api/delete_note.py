from api.base_api import BaseApi


class DeleteNote(BaseApi):
    def __init__(self, token):
        self.ENDPOINT = "/api/notes"
        self.token = token

    def delete_note(self, need_toke, id_note):
        return self._requests(method="DELETE", endpoint=self.ENDPOINT, need_token=need_toke, note_id=id_note)

from api.base_api import BaseApi


class DeleteNote(BaseApi):
    def __init__(self, token):
        self.ENDPOINT_3 = "/api/notes"
        self.token = token

    def delete_notes(self, id_node):
        return self._requests("DELETE", endpoint=self.ENDPOINT_3, need_token=True, note_id=id_node)

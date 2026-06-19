from base_api import BaseApi


class DeleteNote(BaseApi):
    ENDPOINT_3 = "/api/notes"

    def __init__(self, bearer_token):
        super().__init__(bearer_token)

    def delete_notes(self, id_node):
        return self._requests("DELETE", endpoint=self.ENDPOINT_3, need_token=True, note_id=id_node)

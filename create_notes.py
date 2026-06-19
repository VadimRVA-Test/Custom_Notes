from base_api import BaseApi


class CreateNotes(BaseApi):
    ENDPOINT_3 = "/api/notes"

    def __init__(self, bearer_token):
        super().__init__(bearer_token)

    def create_notes(self, content, title):
        body_note = {"content": content, "title": title}
        return self._requests("POST", endpoint=self.ENDPOINT_3, need_token=True, json=body_note)

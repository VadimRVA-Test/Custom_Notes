from base_api import BaseApi


class GetNotes(BaseApi):
    def __init__(self, token=None):
        super().__init__(token)
        self.ENDPOINT_3 = "/api/notes"

    def get_all_notes(self):
        return self._requests("GET", endpoint=self.ENDPOINT_3, need_token=True)

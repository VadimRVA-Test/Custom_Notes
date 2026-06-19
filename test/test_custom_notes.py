class TestNotes:

    def test_create_notes(self, create_notes):
        assert create_notes.json()["message"] == "Заметка создана!", (
            f"Ожидали сообщение Заметка создана!, получили {create_notes.json()["message"]}")
        assert create_notes.status_code == 201,  (
            f"Ожидали статус код 201, получили {create_notes.status_code}")

    def test_get_notes(self, get_notes):
        assert type(get_notes.json()) == list, (
            f"Ожидали получить тип данных Словарь!, получили {list(get_notes.json())}")
        assert get_notes.status_code == 200, (
            f"Ожидали статус код 200, получили {get_notes.status_code}")

    def test_delete_notes(self, delete_note):
        assert delete_note.status_code == 200, (
            f"Ожидали статус код 200, получили {delete_note.status_code}")
        assert delete_note.json()["message"] == "Note deleted!", (
            f"Ожидали сообщение Note deleted!!, получили {delete_note.json()["message"]}")

    def test_create_delete_after_test(self, create_delete_a):
        assert create_delete_a.json()["message"] == "Заметка создана!", (
            f"Ожидали сообщение Заметка создана!, получили {create_delete_a.json()["message"]}")
        assert create_delete_a.status_code == 201, (
            f"Ожидали статус код 201, получили {create_delete_a.status_code}")

from conftest import authorization


class TestNotes:

    def test_create_notes(self, obj_create_notes, create_notes):
        response = obj_create_notes.create_notes_201(create_notes)
        assert response.status_code == 201
        assert response.json()["message"] == "Заметка создана!"

    def test_create_notes_status_code_401(self, obj_create_notes, create_notes):
        response = obj_create_notes.create_notes_401(create_notes)
        assert response.status_code == 201, (
            f"Ожидали статус код: 201, получили: {create_notes.status_code}")

    def test_create_notes_401_message(self, obj_create_notes, create_notes):
        response = obj_create_notes.create_notes_401(create_notes)
        assert response.json()["message"] == "Заметка создана!", (
            f"Ожидали получить сообщение: Заметка создана! Получили: {response.json()["message"]}")

    def test_create_notes_status_code_403(self, obj_create_notes, create_notes):
        response = obj_create_notes.create_notes_403(create_notes)
        assert response.status_code == 201, (
            f"Ожидали статус код: 201 Получили: {response.status_code}")

    def test_create_notes_403_message(self, obj_create_notes, create_notes):
        response = obj_create_notes.create_notes_403(create_notes)
        assert response.json()["message"] == "Заметка создана!", (
            f"Ожидали получить сообщение: Заметка создана! Получили: {response.json()["message"]}")

    def test_get_notes(self, obj_get_notes):
        response = obj_get_notes.get_all_notes_status_code_200()
        assert response.status_code == 200
        assert type(response.json()) == list

    def test_get_notes_status_code_401(self, obj_get_notes):
        response = obj_get_notes.get_all_notes_status_code_401()
        assert response.status_code == 200, (
            f"Ожидали статус код: 200 Получили: {response.status_code}")

    def test_get_notes_401_message(self, obj_get_notes):
        response = obj_get_notes.get_all_notes_status_code_401()
        assert type(response.json()["message"]) == list, (
            f"Ожидали получить сообщение:Успешное получение заметок Получили: {response.json()["message"]}")

    def test_get_notes_status_code_403(self, obj_get_notes):
        response = obj_get_notes.get_all_notes_status_code_403()
        assert response.status_code == 200, (
            f"Ожидали статус код: 200 Получили: {response.status_code}")

    def test_get_notes_403_message(self, obj_get_notes):
        response = obj_get_notes.get_all_notes_status_code_403()
        assert type(response.json()["message"]) == list, (
            f"Ожидали получить сообщение:Успешное получение заметок Получили: {response.json()["message"]}")

    def test_delete_notes(self, obj_delete_note, id_note):
        response = obj_delete_note.delete_notes_status_code_200(id_note)
        assert response.status_code == 200
        assert response.json()["message"] == "Note deleted!"

    def test_delete_notes_status_code_401(self, obj_delete_note, id_note):
        response = obj_delete_note.delete_notes_status_code_401(id_note)
        assert response.status_code == 200, (
            f"Ожидали статус код: 200 Получили: {response.status_code}")

    def test_delete_notes_401_message(self, obj_delete_note, id_note):
        response = obj_delete_note.delete_notes_status_code_401(id_note)
        assert response.json()["message"] == "Note deleted!", (
            f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")

    def test_delete_notes_status_code_403(self, obj_delete_note, id_note):
        response = obj_delete_note.delete_notes_status_code_403(id_note)
        assert response.status_code == 200, (
            f"Ожидали статус код: 200 Получили: {response.status_code}")

    def test_delete_notes_403_message(self, obj_delete_note, id_note):
        response = obj_delete_note.delete_notes_status_code_403(id_note)
        assert response.json()["message"] == "Note deleted!", (
            f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")

    def test_delete_notes_status_code_409(self, id_note, obj_delete_note_409):
        response = obj_delete_note_409.delete_notes_status_code_200(id_note)
        assert response.status_code == 200, (
            f"Ожидали статус код: 200 Получили: {response.status_code}")

    def test_delete_notes_409_message(self, id_note, obj_delete_note_409):
        response = obj_delete_note_409.delete_notes_status_code_200(id_note)
        assert response.json()["message"] == "Note deleted!", (
            f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")

    def test_create_delete_after_test(self, setup_teardown_note, obj_create_notes, create_notes):
        response = obj_create_notes.create_notes_201(create_notes)
        assert response.json()["message"] == "Заметка создана!", (
            f"Ожидали сообщение Заметка создана!, получили {response.json()["message"]}")
        assert response.status_code == 201, (
            f"Ожидали статус код 201, получили {response.status_code}")
        print(setup_teardown_note)

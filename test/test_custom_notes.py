from test.conftest import second_token
from test.data.json_for_post import body_note


class TestNotes:

    def test_create_note(self, obj_create_note, obj_get_notes, teardown_note):
        response = obj_create_note.create_note(True, body_note)
        assert response.status_code == 201, f"Ожидали получить статус код: 201, получили: {response.status_code}"
        assert response.json()["message"] == "Заметка создана!", (
            f"Ожидали получить сообщение: Заметка создана! Получили: {response.json()["message"]}")
        id_note = obj_get_notes.get_not_id_by_title(True, body_note["title"])
        teardown_note.append(id_note)

    def test_create_notes_token_is_empty(self, obj_create_note):
        response = obj_create_note.create_note(False, body_note)
        assert response.status_code == 401, f"Ожидали статус код: 401, получили: {response.status_code}"
        assert response.json()["message"] == "Token is missing!", (
            f"Ожидали получить сообщение: Token is missing!"
            f"Получили: {response.json()["message"]}")

    def test_create_notes_invalid_token(self, obj_create_note):
        obj_create_note.token = ""
        response = obj_create_note.create_note(True, body_note)
        assert response.status_code == 403, f"Ожидали статус код: 403 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is invalid or expired!", (
            f"Ожидали получить сообщение:Token is invalid or expired!"
            f"Получили: {response.json()["message"]}")

    def test_get_notes(self, obj_get_notes, setup_teardown_note):
        response = obj_get_notes.get_all_notes(True)
        assert response.status_code == 200, f"Ожидали получить статус код: 200, получили: {response.status_code}"
        assert type(response.json()) == list, f"Ожидали получить тип данных список, получили: {type(response.json())}"
        assert len(response.json()) > 0, f"Ожидали получить количество элементов > 0, Получили: {len(response.json())}"

    def test_get_notes_token_is_empty(self, obj_get_notes):
        response = obj_get_notes.get_all_notes(False)
        assert response.status_code == 401, f"Ожидали статус код: 401 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is missing!", (
            f"Ожидали получить сообщение:Успешное получение заметок Получили: {response.json()["message"]}")

    def test_get_notes_invalid_token(self, obj_get_notes):
        obj_get_notes.token = ""
        response = obj_get_notes.get_all_notes(True)
        assert response.status_code == 403, f"Ожидали статус код: 403 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is invalid or expired!", (
            f"Ожидали получить сообщение:Token is invalid or expired!"
            f" Получили: {response.json()["message"]}")

    def test_delete_note(self, obj_delete_note, id_note, obj_get_notes):
        print(id_note)
        response = obj_delete_note.delete_note(True, id_note)
        assert response.status_code == 200, f"Ожидали статус код: 200 Получили: {response.status_code}"
        assert response.json()["message"] == "Note deleted!", (
            f"Ожидали получить сообщение:Note deleted! Получили: {response.json()["message"]}")
        response2 = obj_delete_note.delete_note(True, id_note)
        assert response2.status_code == 404, f"Ожидали статус код: 200 Получили: {response2.status_code}"

    def test_delete_notes_token_is_empty(self, obj_delete_note, setup_teardown_note):
        response = obj_delete_note.delete_note(False, setup_teardown_note)
        assert response.status_code == 401, f"Ожидали статус код: 401 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is missing!", (
            f"Ожидали получить сообщение: Token is missing! Получили: {response.json()["message"]}")

    def test_delete_notes_invalid_token(self, obj_delete_note, setup_teardown_note):
        obj_delete_note.token = "shg"
        response = obj_delete_note.delete_note(True, setup_teardown_note)
        assert response.status_code == 403, f"Ожидали статус код: 403 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is invalid or expired!", (
            f"Ожидали получить сообщение: Token is invalid or expired! Получили: {response.json()["message"]}")

    def test_del_notes_resource_conflict(self, setup_teardown_note, obj_delete_note, second_token):
        obj_delete_note.token = second_token
        response = obj_delete_note.delete_note(True, setup_teardown_note)
        assert response.status_code == 409, f"Ожидали статус код: 409 Получили: {response.status_code}"
        assert response.json()["message"] == "Not authorized to delete this note", (
            f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")

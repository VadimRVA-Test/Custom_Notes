from data.json_for_post import body_note


class TestNotes:

    def test_create_note(self, obj_create_note, obj_get_notes, teardown_note):
        need_token = True
        note = {"content": body_note["content"], "title": body_note["title"]}
        response = obj_create_note.create_note(need_token,  body_note)
        assert response.status_code == 201, f"Ожидали получить статус код: 201, получили: {response.status_code}"
        assert response.json()["message"] == "Заметка создана!", (
            f"Ожидали получить сообщение: Заметка создана! Получили: {response.json()["message"]}")
        id_note = obj_get_notes.get_not_id_by_title(need_token, note["title"])
        teardown_note.append(id_note)

    def test_create_notes_token_is_empty(self, obj_create_note):
        need_token = False
        note = {"content": body_note["content"], "title": body_note["title"]}
        response = obj_create_note.create_note(need_token, note)
        assert response.status_code == 401, f"Ожидали статус код: 401, получили: {response.status_code}"
        assert response.json()["message"] == "Token is missing!", (
            f"Ожидали получить сообщение: Token is missing!"
            f"Получили: {response.json()["message"]}")

    def test_create_notes_invalid_token(self, obj_create_note):
        need_token = True
        obj_create_note.token = ""
        note = {"content": body_note["content"], "title": body_note["title"]}
        response = obj_create_note.create_note(need_token, note)
        assert response.status_code == 403, f"Ожидали статус код: 403 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is invalid or expired!", (
            f"Ожидали получить сообщение:Token is invalid or expired!"
            f"Получили: {response.json()["message"]}")

    def test_get_notes(self, obj_get_notes):
        need_token = True
        response = obj_get_notes.get_all_notes(need_token)
        assert response.status_code == 200, f"Ожидали получить статус код: 200, получили: {response.status_code}"
        assert type(response.json()) == list, f"Ожидали получить тип данных список, получили: {type(response.json())}"

    def test_get_notes_token_is_empty(self, obj_get_notes):
        need_token = False
        response = obj_get_notes.get_all_notes(need_token)
        assert response.status_code == 401, f"Ожидали статус код: 401 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is missing!", (
            f"Ожидали получить сообщение:Успешное получение заметок Получили: {response.json()["message"]}")

    def test_get_notes_invalid_token(self, obj_get_notes):
        need_token = True
        obj_get_notes.token = ""
        response = obj_get_notes.get_all_notes(need_token)
        assert response.status_code == 403, f"Ожидали статус код: 403 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is invalid or expired!", (
            f"Ожидали получить сообщение:Token is invalid or expired!"
            f" Получили: {response.json()["message"]}")

    def test_delete_note(self, obj_delete_note, id_note):
        need_token = True
        response = obj_delete_note.delete_note(need_token, id_note)
        assert response.status_code == 200, f"Ожидали статус код: 200 Получили: {response.status_code}"
        assert response.json()["message"] == "Note deleted!", (
            f"Ожидали получить сообщение:Note deleted! Получили: {response.json()["message"]}")

    def test_delete_notes_token_is_empty(self, obj_delete_note, id_note, teardown_note):
        need_token = False
        response = obj_delete_note.delete_note(need_token, id_note)
        assert response.status_code == 401, f"Ожидали статус код: 401 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is missing!", (
            f"Ожидали получить сообщение: Token is missing! Получили: {response.json()["message"]}")
        teardown_note.append(id_note)

    def test_delete_notes_invalid_token(self, obj_delete_note, id_note, token, teardown_note):
        need_token = True
        obj_delete_note.token = "shg"
        response = obj_delete_note.delete_note(need_token, id_note)
        assert response.status_code == 403, f"Ожидали статус код: 403 Получили: {response.status_code}"
        assert response.json()["message"] == "Token is invalid or expired!", (
            f"Ожидали получить сообщение: Token is invalid or expired! Получили: {response.json()["message"]}")
        obj_delete_note.token = token
        teardown_note.append(id_note)

    def test_del_notes_resource_conflict(self, id_note, obj_delete_note, token, del_resource_conflict, teardown_note):
        need_token = True
        response = obj_delete_note.delete_note(need_token, id_note)
        assert response.status_code == 409, f"Ожидали статус код: 409 Получили: {response.status_code}"
        assert response.json()["message"] == "Not authorized to delete this note", (
            f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")
        obj_delete_note.token = token
        teardown_note.append(id_note)

    def test_delete_note_after_get_all_notes(self, obj_get_notes, setup_teardown_note):
        need_token = True
        response = obj_get_notes.get_all_notes(need_token)
        assert response.status_code == 200, f"Ожидали получить статус код: 200, получили: {response.status_code}"
        assert type(response.json()) == list, f"Ожидали получить тип данных список, получили: {type(response.json())}"

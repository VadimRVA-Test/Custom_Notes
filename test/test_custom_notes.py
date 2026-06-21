from data.json_for_post import body_note


class TestNotes:

    def test_create_notes(self, obj_create_notes):
        note = {"content": body_note["content"], "title": body_note["title"]}
        response = obj_create_notes.create_notes(note)
        if response.status_code == 201:
            assert response.status_code == 201
            assert response.json()["message"] == "Заметка создана!"
        elif response.status_code == 401:
            assert response.json()["message"] == "Токен не указан!", (
                f"Ожидали статус код: 201, получили: {response.status_code}",
                f"Ожидали получить сообщение: Заметка создана! Получили: {response.json()["message"]}")
        elif response.status_code == 403:
            assert response.json()["message"] == "Токен не верный или истёк!", (
                f"Ожидали статус код: 201, получили: {response.status_code}",
                f"Ожидали получить сообщение: Заметка создана! Получили: {response.json()["message"]}")
        else:
            assert response.status_code == 201, (
                f"Ожидали статус код: 201 Получили: {response.status_code}")

    def test_get_notes(self, get_notes):
        response = get_notes.get_all_notes()
        if response.status_code == 200:
            assert response.status_code == 200
            assert type(response.json()) == list
        elif response.status_code == 401:
            assert response.json()["message"] == "Успешное получение заметок", (
                f"Ожидали статус код: 200, получили: {response.status_code}",
                f"Ожидали получить сообщение:Успешное получение заметок Получили: {response.json()["message"]}")
        elif response.status_code == 403:
            assert response.json()["message"] == "Успешное получение заметок", (
                f"Ожидали статус код: 200, получили: {response.status_code}",
                f"Ожидали получить сообщение: Успешное получение заметок Получили: {response.json()["message"]}")
        else:
            assert response.status_code == 200, (
                f"Ожидали статус код: 201 Получили: {response.status_code}")

    def test_delete_notes(self, delete_note, id_note):
        response = delete_note.delete_notes(id_note)
        if response.status_code == 200:
            assert response.status_code == 200
            assert response.json()["message"] == "Note deleted!"
        elif response.status_code == 401:
            assert response.json()["message"] == "Токен не указан!", (
                f"Ожидали статус код: 200, получили: {response.status_code}",
                f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")
        elif response.status_code == 403:
            assert response.json()["message"] == "Токен неверный или истек!", (
                f"Ожидали статус код: 200, получили: {response.status_code}",
                f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")
        elif response.status_code == 409:
            assert response.status_code == 200, (
                f"Ожидали статус код: 200, получили: {response.status_code}",
                f"Ожидали получить сообщение: Note deleted! Получили: {response.json()["message"]}")
        else:
            assert response.status_code == 200, (
                f"Ожидали статус код: 200 Получили: {response.status_code}")

    def test_create_delete_after_test(self, setup_teardown_note, obj_create_notes):
        response = obj_create_notes.create_notes(body_note)
        assert response.json()["message"] == "Заметка создана!", (
            f"Ожидали сообщение Заметка создана!, получили {response.json()["message"]}")
        assert response.status_code == 201, (
            f"Ожидали статус код 201, получили {response.status_code}")
        print(setup_teardown_note)

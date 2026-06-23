import pytest
from api.registration_users import RegistrationUsers
from api.authorization_users import AuthorizationUsers
from data.json_for_post import data_user, data_user2, body_note
from api.get_notes import GetNotes
from api.create_notes import CreateNotes
from api.delete_notes import DeleteNote


@pytest.fixture
def obj_registration():
    return RegistrationUsers()


@pytest.fixture
def registration(obj_registration):
    email, password, username = data_user["email"], data_user["password"], data_user["username"]
    response = obj_registration.registration_user(email, password, username)
    return response


@pytest.fixture
def registration2(obj_registration, obj_authorization):
    email, password, username = data_user2["email"], data_user2["password"], data_user["username"]
    obj_registration.registration_user(email, password, username)
    response = obj_authorization.authorization_user(email, password)
    return response.json()["token"]


@pytest.fixture
def obj_authorization():
    return AuthorizationUsers()


@pytest.fixture
def authorization(obj_authorization):
    email, password = data_user["email"], data_user["password"]
    response = obj_authorization.authorization_user(email, password)
    return response


@pytest.fixture
def token(obj_authorization):
    token = obj_authorization.get_token(email=data_user["email"], password=data_user["password"])
    return token


@pytest.fixture
def obj_create_notes(token):
    return CreateNotes(token)


@pytest.fixture
def create_notes():
    note = {"content": body_note["content"], "title": body_note["title"]}
    return note


@pytest.fixture
def obj_get_notes(token):
    return GetNotes(token)


@pytest.fixture
def obj_delete_note(token):
    return DeleteNote(token)


@pytest.fixture
def obj_delete_note_409(registration2):
    return DeleteNote(registration2)


@pytest.fixture
def id_note(obj_get_notes, obj_create_notes):
    note_id = obj_get_notes.get_all_notes_status_code_200()
    if len(note_id.json()) == 0:
        obj_create_notes.create_notes_201(body_note)
        note_id = obj_get_notes.get_all_notes_status_code_200()
        return note_id.json()[0]["id"]
    return note_id.json()[0]["id"]


@pytest.fixture
def teardown_note(obj_delete_note):
    list_name_nodes = []
    yield list_name_nodes
    for note in list_name_nodes:
        obj_delete_note.delete_notes_status_code_200(note)


@pytest.fixture
def setup_teardown_note(id_note, teardown_note):
    teardown_note.append(id_note)
    return id_note

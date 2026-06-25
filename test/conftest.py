import pytest
from api.registration_users import RegistrationUsers
from api.authorization_users import AuthorizationUsers
from data.json_for_post import data_user, data_user2, body_note
from api.get_notes import GetNotes
from api.create_note import CreateNotes
from api.delete_note import DeleteNote


@pytest.fixture
def obj_registration():
    return RegistrationUsers()


@pytest.fixture
def obj_authorization():
    return AuthorizationUsers()


@pytest.fixture
def token(obj_authorization):
    token = obj_authorization.get_token(email=data_user["email"], password=data_user["password"])
    return token


@pytest.fixture
def obj_create_note(token):
    return CreateNotes(token)


@pytest.fixture
def obj_get_notes(token):
    return GetNotes(token)


@pytest.fixture
def obj_delete_note(token):
    return DeleteNote(token)


@pytest.fixture
def del_resource_conflict(obj_registration, obj_authorization, obj_delete_note):
    email, password, username = data_user2["email"], data_user2["password"], data_user2["username"]
    obj_registration.registration_user(email, password, username)
    token2 = obj_authorization.authorization_user(email, password)
    obj_delete_note.token = token2.json()["token"]
    return obj_delete_note


@pytest.fixture
def id_note(obj_get_notes, obj_create_note):
    need_token = True
    obj_create_note.create_note(need_token, body_note)
    return obj_get_notes.get_not_id_by_title(need_token, body_note["title"])


@pytest.fixture
def teardown_note(obj_delete_note):
    list_name_nodes = []
    need_token = True
    yield list_name_nodes
    for note in list_name_nodes:
        obj_delete_note.delete_note(need_token, note)


@pytest.fixture
def setup_teardown_note(id_note, teardown_note):
    teardown_note.append(id_note)
    return id_note

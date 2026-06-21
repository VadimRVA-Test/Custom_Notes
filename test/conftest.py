import pytest
from api.registration_users import RegistrationUsers
from api.authorization_users import AuthorizationUsers
from data.json_for_post import data_user, body_note
from api.get_notes import GetNotes
from api.create_notes import CreateNotes
from api.delete_notes import DeleteNote


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
def get_notes(token):
    return GetNotes(token)


@pytest.fixture
def obj_create_notes(token):
    return CreateNotes(token)


@pytest.fixture
def delete_note(token):
    return DeleteNote(token)


@pytest.fixture
def id_note(obj_create_notes, get_notes):
    return get_notes.get_not_id_by_title(title=body_note["title"])


@pytest.fixture
def teardown_note(delete_note):
    list_name_nodes = []
    yield list_name_nodes
    for note in list_name_nodes:
        delete_note.delete_notes(note)


@pytest.fixture
def setup_teardown_note(id_note, teardown_note):
    teardown_note.append(id_note)
    return id_note

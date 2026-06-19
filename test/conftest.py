import pytest

from registration_users import RegistrationUsers
from authorization_users import AuthorizationUsers
from data.json_for_post import JSON_User_1, JSON_User_2, body_note
from get_notes import GetNotes
from create_notes import CreateNotes
from delete_notes import DeleteNote


@pytest.fixture
def registration():
    email, password, username = JSON_User_1["email"], JSON_User_1["password"], JSON_User_1["username"]
    response = RegistrationUsers().registration_user(email, password, username)
    return response

@pytest.fixture
def token_user():
    return AuthorizationUsers()

@pytest.fixture
def token(token_user):
    token = token_user.get_token(email=JSON_User_2["email"], password=JSON_User_2["password"])
    return token

@pytest.fixture
def authorization(token_user):
    response_auth = token_user.authorization_j(email=JSON_User_2["email"], password=JSON_User_2["password"])
    return response_auth

@pytest.fixture
def get_notes(token):
    response = GetNotes(token).get_all_notes()
    return response

@pytest.fixture
def create_notes(token):
    response = CreateNotes(token).create_notes(content=body_note["content"], title=body_note["title"])
    return response

@pytest.fixture
def delete_note(token, get_notes):
    if len(get_notes.json()) >= 1:
        response = DeleteNote(token).delete_notes(get_notes.json()[-1]["id"])
    else:
        response = DeleteNote(token).delete_notes(get_notes)
    return response

@pytest.fixture
def create_delete_a(create_notes, token, get_notes):
    yield create_notes
    DeleteNote(token).delete_notes(get_notes.json()[-1]["id"])






import uuid

data_user = {"email": f"{uuid.uuid4().hex}@example.com",
             "password": f"{uuid.uuid4().hex[:3]}",
             "username": f"{uuid.uuid4().hex[:3]}"}
data_user2 = {"email": "sttjl@example.com", "password": "string"}
data_user3 = {"email": "ttjl@example.com", "password": "string"}
body_note = {"content": uuid.uuid4().hex, "title": uuid.uuid4().hex}

import uuid

data_user = {"email": "sttjl@example.com", "password": "string"}
data_user2 = {"email": f"{uuid.uuid4().hex}@example.com",
              "password": f"{uuid.uuid4().hex[:3]}",
              "username": f"{uuid.uuid4().hex[:3]}"}
body_note = {"content": uuid.uuid4().hex, "title": uuid.uuid4().hex}

import pytest
import json
import sys
sys.path.append(".")
from init import create_app

app_test = create_app()

def test_get_users():
  response = app_test.test_client().get("/users")
  json_data = json.loads(response.data)

  assert response.status_code == 200
  assert json_data[0]['email'] == 'ruperto@gmail.com'

def test_show_user():
  response = app_test.test_client().get(f"/users/2")
  json_data = json.loads(response.data)

  assert response.status_code == 200
  assert json_data[0]['email'] == 'mauricio@outlook.com'

def test_create_and_delete_users():
  body = {'email': 'jos@gmail.com', 'password': 'testtest', 'user_id': 43}
  p_response = app_test.test_client().post("/users", data=json.dumps(body))

  assert p_response.status_code == 201

  get_users = json.loads(app_test.test_client().get("/users"))

  assert get_users[-1]['email'] == 'jos@gmail.com'

  d_response = app_test.test_client().delete("/users/43")

  assert d_response._status_code == 204

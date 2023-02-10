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
  body = {'username': 'jeff', 'email': 'jeff@txstate.edu', 'password': 'mah nemh jeff'}
  p_response = app_test.test_client().post("/users", data=body)

  assert p_response.status_code == 201

  user_data = json.loads(app_test.test_client().get("/users").data)

  assert user_data[-1]['email'] == 'jeff@txstate.edu'
  user_id = user_data[-1]['user_id']

  d_response = app_test.test_client().delete(f"/users/{user_id}")

  assert d_response._status_code == 204

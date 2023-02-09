import pytest
import json
import sys
sys.path.append(".")
from init import create_app

app_test = create_app()

def test_get_cards():
  response = app_test.test_client().get("/cards")
  json_data = json.loads(response.data)

  assert response.status_code == 200
  assert json_data[0]['card_name'] == 'Tepig'

def test_show_card():
  response = app_test.test_client().get(f"/cards/2")
  json_data = json.loads(response.data)

  assert response.status_code == 200
  assert json_data[0]['card_name'] == 'Victini'

def test_create_and_delete_cards():
  body = {'card_name': 'Squirtle', 'hp': 100, "price": 4.3, 'retreat_cost': 1, 'stage': 0, 'card_id': 42}
  p_response = app_test.test_client().post("/users", data=json.dumps(body))

  assert p_response.status_code == 201

  get_cards = json.loads(app_test.test_client().get("/cards"))

  assert get_cards[-1]['card_name'] == 'Squirtle'

  d_response = app_test.test_client().delete("/cards/42")

  assert d_response._status_code == 204
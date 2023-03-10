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
  body = {'name': 'Squirtle', 'hp': 100, "price": 4.3, 'retreat_cost': 1, 'stage': 0}
  p_response = app_test.test_client().post("/cards", data=body)

  assert p_response.status_code == 201

  get_cards = json.loads(app_test.test_client().get("/cards").data)

  assert get_cards[-1]['card_name'] == 'Squirtle'
  card_id = get_cards[-1]['card_id']

  d_response = app_test.test_client().delete(f"/cards/{card_id}")

  assert d_response._status_code == 204
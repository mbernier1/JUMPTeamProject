import pytest
import json
import sys
sys.path.append(".")
from init import create_app

app_test = create_app()

def test_login_logout():
    body = {"email": "ruperto@gmail.com", "password": "save the princess"}
    login_response = app_test.test_client().post("/login", data=body)

    assert login_response.status_code == 200
    
    session_response = app_test.test_client().get("/sessions")
    sessions = json.loads(session_response.data)
    assert len(sessions) > 0

    user_id = sessions[-1]['user_id']

    logout_response = app_test.test_client().delete("/logout", data={"user_id": user_id})
    assert logout_response.status_code == 200



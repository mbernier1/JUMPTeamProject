from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

session_blueprint = Blueprint('sessions', __name__)

# Function to get all users
@session_blueprint.route('/sessions', methods=["GET"])
def get_sessions() -> list[dict]:
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("get_sessions"))
    users = cur.fetchall()
    return users

@session_blueprint.route('/is-loggedin', methods=["GET"])
def is_loggedin() -> bool:
    user_id = request.json.get("user_id")

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("is_loggedin"), [user_id])
    sessions = cur.fetchall()

    return len(sessions) > 0
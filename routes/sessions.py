from flask import Blueprint
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
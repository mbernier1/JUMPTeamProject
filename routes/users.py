from flask import Blueprint
from database import db
from misc.utilities import read_sql

users_blueprint = Blueprint('users', __name__)

# Function to get all users
@users_blueprint.route('/users', methods=["GET"])
def get_all_users() -> list[dict]:
    cur = db.new_cursor(dictionary=True)
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users

# Function to get user by name
@users_blueprint.route('/users/<email>', methods=["GET"])
def get_user_by_name(email):
    try:
        if type(email) != str:
            raise ValueError
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_user_by_name"), [email])
        user = cur.fetchall()
        return user
    except ValueError:
        return "Invalid input", 422

# Function to get user cards
@users_blueprint.route('/users/<user_id>/cards', methods=["GET"])
def get_user_cards(user_id) -> list[dict]:
    try:
        if type(user_id) != str:
            raise ValueError
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_user_cards"), [user_id])
        user = cur.fetchall()
        return user
    except ValueError:
        return "Invalid user input", 422
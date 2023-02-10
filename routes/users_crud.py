from flask import Blueprint, request
from database import db
from misc.utilities import read_sql
import re

users_crud_blueprint = Blueprint('users_crud', __name__)

# Add user to database
@users_crud_blueprint.route('/users', methods=["POST"])
def add_user():

    try:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            return "Invalid Email address", 422

        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("add_new_user"), [username, email, password])
        conn = db.connection
        conn.commit()

        return f"User {username} created", 201
    except:
        return "Invalid inputs", 422

# Update user in database
@users_crud_blueprint.route('/users/<user_id>', methods=["PUT"])
def update_user(user_id):
    try:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            return "Invalid email address", 422

        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("update_user"), [username, email, password, user_id])
        conn = db.connection
        conn.commit()

        return f"User {username} updated", 201
    except:
        return "Invalid input", 422

    
# Delete user from database
@users_crud_blueprint.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        user_id = int(user_id)
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("delete_user"), [user_id])
        conn = db.connection
        conn.commit()

        return f"User deleted", 204
    except ValueError:
        return "Invalid input", 422

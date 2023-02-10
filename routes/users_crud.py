from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

users_crud_blueprint = Blueprint('users_crud', __name__)

# Add user to database
@users_crud_blueprint.route('/users', methods=["POST"])
def add_user():

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("add_new_user"), [username, email, password])
    conn = db.connection
    conn.commit()

    return f"User {username} created", 201

# Update user in database
@users_crud_blueprint.route('/users/<user_id>', methods=["PUT"])
def update_user(user_id):

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("update_user"), [username, email, password, user_id])
    conn = db.connection
    conn.commit()

    return f"User {username} updated", 201

    
# Delete user from database
@users_crud_blueprint.route('/users<user_id>', methods=["DELETE"])
def delete_user(user_id):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("delete_user"), [user_id])
    conn = db.connection
    conn.commit()

    return f"User deleted", 200
from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

users_crud_blueprint = Blueprint('users_crud', __name__)




# Add user to database
@users_crud_blueprint.route('/users<name><email><password>', method=["GET"])
def add_user(name, email, password):
    cur = db.new_cursor(Dictionary=True)
    cur.execute(read_sql("add_new_user"), [name, email, password])

# Update user in database
@users_crud_blueprint.route('/users<name>', method=["POST"])
def update_user(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("update_user"), [name])
    
# Delete user from database
@users_crud_blueprint.route('/users<name>', method=["GET"])
def delete_user(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("delete_user"), [name])
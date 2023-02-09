from flask import Blueprint, request
from database import db
from misc.utilities import read_sq

users_crud_blueprint = Blueprint('users_crud', __name__)




# Add user to database
@users_crud_blueprint.route('/users<name><email><password>', method=["GET"])
def add_user():
    
# Update user in database
@users_crud_blueprint.route('/users', method=["GET"])
def update_user(name):

# Delete user from database
@users_crud_blueprint.route('/users', method=["GET"])
def delete_user(name):

from flask import Blueprint, request
from database import db
from misc.utilities import read_sq

cards_crud_blueprint = Blueprint('cards_crud', __name__)




# Add card to database
@cards_crud_blueprint.route('/cards', method=["GET"])
def add_card():
    
# Update card in database
@cards_crud_blueprint.route('/cards/<name>', method=["POST"])
def update_card(name):
    
# Delete card from database
@cards_crud_blueprint.route('/cards/<name>', method=["GET"])
def delete_card(name):
    
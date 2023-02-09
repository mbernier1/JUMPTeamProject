from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

cards_crud_blueprint = Blueprint('cards_crud', __name__)




# Add card to database
@cards_crud_blueprint.route('/cards<name><stage><retreat_cost><hp><cost>', method=["GET"])
def add_card(name, stage, retreat_cost, hp, cost):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("add_new_card"), [name, stage, retreat_cost, hp, cost])
    
# Update card in database
@cards_crud_blueprint.route('/cards/<name>', method=["POST"])
def update_card(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("update_card"), [name])
    
# Delete card from database
@cards_crud_blueprint.route('/cards/<name>', method=["GET"])
def delete_card(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("delete_card"), [name])

from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

cards_crud_blueprint = Blueprint('cards_crud', __name__)

# Add card to database
@cards_crud_blueprint.route('/cards/<name>-<stage>-<retreat_cost>-<hp>-<cost>', method=["POST"])
def add_card(name, stage, retreat_cost, hp, cost):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("add_new_card"), [name, stage, retreat_cost, hp, cost])

    return "Well done, poggers", 200
    
# Update card in database
@cards_crud_blueprint.route('/cards/<id>/<name>-<stage>-<retreat_cost>-<hp>-<price>', method=["PUT"])
def update_card(id, name, stage, retreat_cost, hp, price):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("update_card"), [name, stage, retreat_cost, hp, price, id])
    
# Delete card from database
@cards_crud_blueprint.route('/cards/<name>', method=["DELETE"])
def delete_card(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("delete_card"), [name])

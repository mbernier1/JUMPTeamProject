from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

cards_crud_blueprint = Blueprint('cards_crud', __name__)

# Add card to database
@cards_crud_blueprint.route('/cards', methods=["POST"])
def add_card():
    print("Here")
    
    name = request.form.get('name')
    stage = request.form.get('stage')
    retreat_cost = request.form.get('retreat_cost')
    hp = request.form.get('hp')
    price = request.form.get('price')

    print(name, stage, retreat_cost, hp, price)
    
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("add_new_card"), [name, stage, retreat_cost, hp, price])
    con = db.connection
    con.commit()

    return "Well done, poggers", 201
    
# Update card in database
@cards_crud_blueprint.route('/cards/<id>/<name>-<stage>-<retreat_cost>-<hp>-<price>', methods=["PUT"])
def update_card(id, name, stage, retreat_cost, hp, price):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("update_card"), [name, stage, retreat_cost, hp, price, id])
    
# Delete card from database
@cards_crud_blueprint.route('/cards/<id>', methods=["DELETE"])
def delete_card(id):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("delete_card"), [int(id)])
    con = db.connection
    con.commit()

    return "Much success", 204
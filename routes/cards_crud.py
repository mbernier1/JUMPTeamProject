from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

cards_crud_blueprint = Blueprint('cards_crud', __name__)

# Add card to database
@cards_crud_blueprint.route('/cards', methods=["POST"])
def add_card():
    
    name = request.form.get('name')
    stage = request.form.get('stage')
    retreat_cost = request.form.get('retreat_cost')
    hp = request.form.get('hp')
    price = request.form.get('price')
    
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("add_new_card"), [name, stage, retreat_cost, hp, price])
    conn = db.connection
    conn.commit()

    return f"Card {name} added", 201
    
# Update card in database
@cards_crud_blueprint.route('/cards/<card_id>', methods=["PUT"])
def update_card(card_id):

    name = request.form.get('name')
    stage = request.form.get('stage')
    retreat_cost = request.form.get('retreat_cost')
    hp = request.form.get('hp')
    price = request.form.get('price')

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("update_card"), [name, stage, retreat_cost, hp, price, card_id])
    conn = db.connection
    conn.commit()

    return f"Card {name} updated", 201
    
# Delete card from database
@cards_crud_blueprint.route('/cards/<id>', methods=["DELETE"])
def delete_card(id):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("delete_card"), [id])
    conn = db.connection
    conn.commit()

    return "Deletion complete", 204

from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

cards_blueprint = Blueprint('cards', __name__)

@cards_blueprint.route('/cards', methods=["GET"])
def get_all_cards() -> list[dict]:
    cur = db.new_cursor(dictionary=True)
    cur.execute("SELECT * FROM cards")
    cards = cur.fetchall()

    return cards

@cards_blueprint.route("/cards/<name>", methods=["GET"])
def get_card_by_id(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("get_card_by_name"), [name])
    cards = cur.fetchall()
    return cards


#--------------------------------------------------------------
# I, Mike, added these, I hope they are right


# Function to query cards by type
@cards_blueprint.route("/cards/<type>", methods=["GET"])
def get_cards_by_type(type):
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_type"), [type])
        cards_by_type = cur.fetchall()
        return cards_by_type


# Function to query cards by hp
@cards_blueprint.route("/cards/<hp>", methods=["GET"])
def get_cards_by_hp(hp):
        try:
            if type(hp) != int:
                raise ValueError

            cur = db.new_cursor(dictionary=True)
            cur.execute(read_sql("get_card_by_hp"), [hp])
            cards_by_hp = cur.fetchall()
            return cards_by_hp
        except ValueError:
            return "Invalid input for HP", 422

# Function to query cards by price
@cards_blueprint.route("/cards/<price>", methods=["GET"])
def get_cards_by_price(price):
    try:
        if type(price) != float:
            raise ValueError
        
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_price"), [price])
        cards_by_price = cur.fetchall()
        return cards_by_price
    except:
        return "Invalid input for Price", 422
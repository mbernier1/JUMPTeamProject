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
    try:
        if type(name) != str:
            raise ValueError
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_name"), [name])
        cards = cur.fetchall()
        return cards
    except ValueError:
        return "Invalid input for name", 422


#--------------------------------------------------------------
# I, Mike, added these, I hope they are right
# I, John, also hope they are right


# Function to query cards by type
@cards_blueprint.route("/cards/<type>", methods=["GET"])
def get_cards_by_type(type):
    try:
        if type(type) != str:
            raise ValueError
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_type"), [type])
        cards_by_type = cur.fetchall()
        return cards_by_type
    except ValueError:
        return "Invalid input for type", 422


# Function to query cards by hp
@cards_blueprint.route("/cards/<hpmin>-<hpmax>", methods=["GET"])
def get_cards_by_hp(hpmin, hpmax):
        try:
            if type(hpmin) != int or type(hpmax) != int or not hpmin < hpmax:
                raise ValueError

            cur = db.new_cursor(dictionary=True)
            cur.execute(read_sql("get_card_by_hp"), [hpmin, hpmax])
            cards_by_hp = cur.fetchall()
            return cards_by_hp
        except ValueError:
            return "Invalid input for HP", 422

# Function to query cards by price
@cards_blueprint.route("/cards/<pricemin>-<pricemax>", methods=["GET"])
def get_cards_by_price(pricemin, pricemax):
    try:
        if type(pricemin) != float or type(pricemax) != float or not pricemin < pricemax:
            raise ValueError
        
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_price"), [pricemin, pricemax])
        cards_by_price = cur.fetchall()
        return cards_by_price
    except:
        return "Invalid input for Price", 422
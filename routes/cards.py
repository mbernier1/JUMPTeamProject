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

@cards_blueprint.route("/cards/<id>", methods=["GET"])
def get_card_by_id(id):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("get_card_by_id"), [id])
    cards = cur.fetchall()
    return cards

@cards_blueprint.route("/cards/search/<name>", methods=["GET"])
def get_card_by_name(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("get_card_by_name"), [name])
    cards = cur.fetchall()
    return cards

#--------------------------------------------------------------
# I, Mike, added these, I hope they are right
# I, John, also hope they are right


# Function to query cards by type
@cards_blueprint.route("/cards/<cardtype>", methods=["GET"])
def get_cards_by_type(cardtype):
    try:
        if not cardtype.isalpha():
            raise ValueError
    except ValueError:
        return "Invalid input for type", 422
    else:
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_type"), [type])
        cards_by_type = cur.fetchall()
        return cards_by_type


# Function to query cards by hp
@cards_blueprint.route("/cards/hp/<hpmin>-<hpmax>", methods=["GET"])
def get_cards_by_hp(hpmin, hpmax):
    try:
        hpmin = int(hpmin)
        hpmax = int(hpmax)
        if not hpmin < hpmax:
            raise ValueError
    except ValueError:
        return "Invalid hp inputs", 422
    else:
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_hp"), [hpmin, hpmax])
        cards_by_hp = cur.fetchall()
        return cards_by_hp

# Function to query cards by price
@cards_blueprint.route("/cards/prices/<pricemin>-<pricemax>", methods=["GET"])
def get_cards_by_price(pricemin, pricemax):
    try:
        pricemin = float(pricemin)
        pricemax = float(pricemax)
        if pricemin < pricemax:
            raise ValueError
    except ValueError:
        return "Invalid input for price", 422
    else:
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_by_price"), [pricemin, pricemax])
        cards_by_price = cur.fetchall()
        return cards_by_price
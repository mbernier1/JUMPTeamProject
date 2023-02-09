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

# Function to query cards by type

# Function to query cards by hp

# Function to query cards by price
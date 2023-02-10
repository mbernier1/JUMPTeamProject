from flask import Blueprint
from database import db
from misc.utilities import read_sql
import re

reviews_blueprint = Blueprint('reviews', __name__)

# Function to get reviews by card
@reviews_blueprint.route('/reviews/<cname>', methods=['GET'])
def get_card_reviews(cname):
    try:
        cname = int(cname)
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_card_reviews"), [cname])
        reviews = cur.fetchall()
        return reviews
    except ValueError:
        return "Invalid card name", 422

# Function to get reviews by user
@reviews_blueprint.route('/reviews/<email>', methods=['GET'])
def get_user_reviews(email):
    try:
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            raise ValueError
        cur = db.new_cursor(dictionary=True)
        cur.execute(read_sql("get_user_reviews"), [email])
        reviews = cur.fetchall()
        return reviews
    except ValueError:
        return "Invalid email address", 422
from flask import Blueprint, request
from database import db
from misc.utilities import read_sql
import re

authentication_blueprint = Blueprint('auth', __name__)

@authentication_blueprint.route("/login", methods=["POST"])
def login():
    email = request.json.get('email')
    password =request.json.get('password')

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("verify_user"), [email, password])
    res = cur.fetchall()

    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
        return "Invalid email address", 422
    if len(res) == 0:
        return "No match for username and password found", 404


    user = res[0]
    cur.execute(read_sql("store_user_session"), [user['user_id']])
    conn = db.connection
    conn.commit()
    
    return {'user_id': user['user_id']}, 200

@authentication_blueprint.route("/logout", methods=["POST"])
def logout():
    user_id = request.json.get('user_id')

    if not user_id:
        return "No user login data", 400

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("remove_user_session"), [user_id])
    conn = db.connection
    conn.commit()

    return "Logged out", 200

@authentication_blueprint.route("/signup", methods=["POST"])
def signup():
    username = request.json.get('username')
    email = request.json.get('email')
    password =request.json.get('password')

    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
        return "Invalid email address", 422

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("add_new_user"), [username, email, password])
    conn = db.connection
    conn.commit()

    return "User created", 201
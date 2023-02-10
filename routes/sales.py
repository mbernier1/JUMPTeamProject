from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

sales_blueprint = Blueprint('sales', __name__)

# Get all sales
@sales_blueprint.route('/sales', methods=['GET'])
def handle_all_sales_request() -> list[dict]:
    cursor = db.new_cursor(dictionary=True)
    cursor.execute(read_sql("get_all_sales"))
    sales = cursor.fetchall()

    return sales

# Get cards and how many times they've been sold
@sales_blueprint.route('/sales/<id>', methods=['GET'])
def handle_sales_retrieval(id:str):

    if id.isnumeric():
        cursor = db.new_cursor(dictionary=True)
        cursor.execute(read_sql("get_sale_by_id"), [id])
        sale = cursor.fetchall()
        return sale

    return "ID does not exist or is invalid"

# Get purchases by user

@sales_blueprint.route('/sales/user/<id>', methods=['GET'])
def handle_sales_by_user_id(id):
    if id.isnumeric():
        cursor = db.new_cursor(dictionary=True)
        cursor.execute(read_sql("get_sales_by_user_id"), [id])
        sale = cursor.fetchall()
        return sale

    return "ID is invalid"
from flask import Blueprint, request
from database import db
from misc.utilities import read_sql
<<<<<<< HEAD
import datetime
=======
>>>>>>> d4026f778848beb2782b70a5d368007abcb3b95c

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

    return "Sales ID does not exist or is invalid"

# Get purchases by user
@sales_blueprint.route('/sales/user/<id>', methods=['GET'])
def handle_sales_by_user_id(id):
    if id.isnumeric():
        cursor = db.new_cursor(dictionary=True)
        cursor.execute(read_sql("get_sales_by_user_id"), [id])
        sale = cursor.fetchall()
        return sale

    return "ID is invalid"

# Handling inserting and updating a new record
@sales_blueprint.route('/sales/handle_sale/', methods=['POST', 'PUT', 'DELETE'])
def handle_add_new_sale():

    if request.method == 'POST':
        print("Post initiated")
        try:
            user_id = request.json.get('user_id')
            items = request.json.get('items')
            date = str(datetime.datetime.now().date())
            
            cursor = db.new_cursor(dictionary=True)
            cursor.execute(read_sql('create_sale_record'), [user_id, date])
            new_record_id = cursor.lastrowid

            card_sales = []
            for i in items:
                card_sales.append((int(i), int(new_record_id)))
            
            cursor.executemany(read_sql('append_card_sales'), card_sales)

            db.connection.commit()

        except Exception as e:
            # Log exception
            print(str(e))
            return "Error handling update"

        else:
            return "Sales added successfully"


    if request.method == "PUT":
        print("Update requested")
        try:
            # user_id = request.json.get('user_id')
            transaction_id = request.json.get('transaction_id')
            items = request.json.get('items')

            if transaction_id is None: raise Exception("Unable to identify sales id")

            cursor = db.new_cursor(dictionary=True)
            # cursor.execute("Select sale_id from sales where sales.sale_id=%s", [transaction_id])
            cursor.execute(read_sql("get_sales_id_by_sales_id"), [transaction_id])

            if cursor.fetchone() is None: raise Exception("Sales transaction does not exist")

            cursor.execute(read_sql("delete_record_from_card_sales"), [transaction_id])
            
            card_sales = []
            for i in items:
                card_sales.append((int(i), int(transaction_id)))
            cursor.executemany(read_sql('append_card_card_sales'), card_sales)

            db.connection.commit()
        
        except Exception as e:
            print(str(e))
            return "Unable to process request"

        else:
            return "Sales updated successfully"

    if request.method == "DELETE":
        try:
            transaction_id = request.json.get('transaction_id')
            if transaction_id is None: raise Exception("Unable to identify sales id")

            cursor = db.new_cursor(dictionary=True)
            # cursor.execute("Select sale_id from sales where sales.sale_id=%s", [transaction_id])
            cursor.execute(read_sql("get_sales_id_by_sales_id"), [transaction_id])
            if cursor.fetchone() is None: raise Exception("Sales transaction does not exist")

            cursor.execute(read_sql("delete_record_from_card_sales"), [transaction_id])
            cursor.execute("Delete from sales where sales.sale_id=%s", [transaction_id])

            db.connection.commit()

        except Exception as e:
            print(str(e))
            return "An error has ocurred while handling your request"
        else:
            return "Sales record has been deleted successfully"
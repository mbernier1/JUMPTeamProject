from flask import Blueprint, request
from database import db
from misc.utilities import read_sql
import datetime

sales_blueprint = Blueprint('sales', __name__)


@sales_blueprint.route('/sales', methods=['GET'])
def handle_all_sales_request() -> list[dict]:

    try:
        cursor = db.new_cursor(dictionary=True)
        cursor.execute(read_sql("get_all_sales"))
        sales = cursor.fetchall()
    except Exception as e:
        print(str(e))
        return "Unable to fetch requested data", 500
    else:
        return sales, 200


@sales_blueprint.route('/sales/<id>', methods=['GET'])
def handle_sales_retrieval(id: str):

    try:
        if not id.isnumeric():
            raise ValueError("Invalid id provided")

        cursor = db.new_cursor(dictionary=True)
        cursor.execute(read_sql("get_sale_by_id"), [id])
        sale = cursor.fetchall()

        if len(sale) == 0:
            raise Exception("No results found")

    except ValueError as e:
        print(str(e))
        return "Invalid id provided", 400
    except Exception as e:
        print(str(e))
        return "Sales ID does not exist", 400
    else:
        return sale, 200


@sales_blueprint.route('/sales/user/<id>', methods=['GET'])
def handle_sales_by_user_id(id):
    try:

        if not id.isnumeric():
            raise ValueError("Invalid ID")
        cursor = db.new_cursor(dictionary=True)
        cursor.execute(read_sql("get_sales_by_user_id"), [id])
        sale = cursor.fetchall()

    except ValueError as e:
        print(str(e))
        return str(e), 400
    else:
        return sale, 200



@sales_blueprint.route('/sales/handle-sale', methods=['POST', 'PUT', 'DELETE'])
def handle_add_new_sale():
    print("Here")
    if request.method == 'POST':
        try:
            user_id = request.json.get('user_id')
            items = request.json.get('items')
            date = str(datetime.datetime.now().date())

            print(user_id)
            print(items)

            cursor = db.new_cursor(dictionary=True)
            cursor.execute(read_sql('create_sale_record'), [user_id, date])
            sale_id = cursor.lastrowid

            card_sales = []
            for card_id in items:
                card_sales.append((int(card_id), int(sale_id)))

            cursor.executemany(read_sql('append_card_sales'), card_sales)

            cursor.execute(read_sql('get_user_cards'), [user_id])
            user_cards = cursor.fetchall()
            print(len(user_cards))
            existing_card = list(filter(lambda card: card['card_id'] == items[0], user_cards))
            
            if len(existing_card) > 0:
                print("Updated quantity")
                cursor.execute(read_sql("increase_inv_count"), [card_id])
            else:
                card_inventory = []
                for card_id in items:
                    card_inventory.append((int(user_id), int(card_id)))
                cursor.executemany(read_sql('add_card_inventory'), card_inventory)


            db.connection.commit()

        except Exception as e:
            print(str(e))
            return "Error handling post"

        else:
            return {user_id: user_id, card_id: card_id}, 200

    if request.method == "PUT":

        try:

            transaction_id = request.json.get('transaction_id')
            items = request.json.get('items')

            if transaction_id is None:
                raise Exception("Unable to identify sales id")

            cursor = db.new_cursor(dictionary=True)

            cursor.execute(read_sql("get_sales_id_by_sales_id"),
                           [transaction_id])

            if cursor.fetchone() is None:
                raise Exception("Sales transaction does not exist")

            cursor.execute(read_sql("delete_record_from_card_sales"), [
                           transaction_id])

            card_sales = []
            for i in items:
                card_sales.append((int(i), int(transaction_id)))
            cursor.executemany(read_sql('append_card_sales'), card_sales)

            db.connection.commit()

        except Exception as e:
            print(str(e))
            return "Unable to process request"

        else:
            return "Sales updated successfully"

    if request.method == "DELETE":
        try:
            transaction_id = request.json.get('transaction_id')
            if transaction_id is None:
                raise Exception("Unable to identify sales id")

            cursor = db.new_cursor(dictionary=True)

            cursor.execute(read_sql("get_sales_id_by_sales_id"),
                           [transaction_id])
            if cursor.fetchone() is None:
                raise Exception("Sales transaction does not exist")

            cursor.execute(read_sql("delete_record_from_card_sales"), [
                           transaction_id])
            cursor.execute("Delete from sales where sales.sale_id=%s", [
                           transaction_id])

            db.connection.commit()

        except Exception as e:
            print(str(e))
            return "An error has ocurred while handling your request"
        else:
            return "Sales record has been deleted successfully"

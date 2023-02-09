from flask import Flask, jsonify, request
import pokemon_data as pokemon



app = Flask(__name__)


# read all pokemon cards
@app.route("/cards", methods=["GET"])
def get_all_cards():
    return jsonify(pokemon.read_all_cards())

# Create a card
@app.route("/cards", methods=["POST"])
def create_a_card():
    data = request.get_json()
    pokemon.create_new_pokemon_card(data)
    return "New pokemon added"
    
        
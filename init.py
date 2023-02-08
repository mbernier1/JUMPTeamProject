from flask import Flask 

app = Flask(__name__)

@app.route('/cards')
def get_all_cards():
    return 'all cards'
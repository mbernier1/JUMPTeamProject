from flask import Flask 

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABSE'] = 'pokemon_db'

@app.route('/cards', methods=["GET"])
def get_all_cards():
    return 'all cards'

if __name__ == "__main__":
    app.run(port=8080)
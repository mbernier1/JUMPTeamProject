from flask import Flask 

app = Flask(__name__)

@app.route('/cards', methods=["GET"])
def get_all_cards():
    return 'all cards'

if __name__ == "__main__":
    app.run(port=8080)
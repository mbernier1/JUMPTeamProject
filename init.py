from flask import Flask 
from database import db
from KEYS import USER, DATABASE, PASSWORD
from routes.cards import cards_blueprint
from routes.users import users_blueprint
from routes.sales import sales_blueprint

def create_app():

    app = Flask(__name__)
    app.config['MYSQL_DATABASE'] = DATABASE
    app.config['MYSQL_USER'] = USER
    app.config['MYSQL_PASSWORD'] = PASSWORD

    db.init_app(app)

    @app.route("/", methods=["GET"])
    def hello():
        return "Welcome to the Pokemon Card Bootleg Market 🥴"

    app.register_blueprint(cards_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(sales_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=8080, debug=True)
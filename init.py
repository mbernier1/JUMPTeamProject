from flask import Flask 
from database import db
from KEYS import USER, DATABASE, PASSWORD
from routes.cards import cards_blueprint
from routes.users import users_blueprint
from routes.sales import sales_blueprint
from routes.reviews import reviews_blueprint
from routes.cards_crud import cards_crud_blueprint
from routes.users_crud import users_crud_blueprint

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
    app.register_blueprint(reviews_blueprint)
    app.register_blueprint(cards_crud_blueprint)
    app.register_blueprint(users_crud_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=8080, debug=True)
from flask import Flask, request, jsonify, make_response 
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity  
from flask_cors import CORS
from models import db, User, Product, Category, Brand, Invoice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'the-key-is-secret'

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)
CORS(app)
jwt = JWTManager(app)


class Home(Resource):
    def get(self):
        response_message = {
            "message": "Welcome to the Bloom Beauty Management System API"
        }
        return make_response(response_message, 200)



api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(port=5555)
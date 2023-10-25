from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata = metadata)

class User(db.model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    ph_address= db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    city_town = db.Column(db.String(100), nullable=False)

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(255), nullable=False)
    p_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable = False)
    category = 
    
class Category (db.Model, SerializerMixin):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    cat_name = db.Column(db.String(150), nullable =False)
    
from app import app, db
from models import User, Product, Brand, Category, Invoice
from datetime import datetime
from sqlalchemy.orm import sessionmaker

with app.app_context():
    def delete_data():
    #this deletes existing db data in columns 
        print("Delete_data...")
        User.query.delete()
        Product.query.delete()
        Brand.query.delete()
        Invoice.query.delete()
        
    
    def seed_data():
        print("🦸 Seeding User data...")
        user1 =User(first_name="kenya", last_name="kwanza", username = "yudiye", email="kenyakwanza@mail.com", ph_address = "Statehouse Road, Kilimani", password="kwisha2023", telephone = "254712345678", city_town = "Nairobi")
        user2 =User(first_name="john", last_name="doe", username = "johndoe23", email="johndoe@mail.com", ph_address = "Muthurwa, Kamukunji", password="john2023", telephone = "254712345679", city_town = "Nairobi")

        user_list =[user1, user2]
        db.session.add_all(user_list)
    
        print("🦸‍♀️ Seeding Brands...")
        brand_1 = Brand(brand_name = "Huddah Cosmetics", brand_logo = "some url for her cosmetics logo here")
        brand_2 = Brand(brand_name = "Rihanna", brand_logo = "Rihannas logo here")
        
        brands_list = [brand_1, brand_2]
        db.session.add_all(brands_list)
        
        print("🦸‍♀️ Seeding Categories...")
        category_1 = Category(cat_name = "Lipstick")
        category_2 = Category(cat_name = "Face")
        category_3 = Category(cat_name = "Eyes")
        category_4 = Category(cat_name = "Make-up")
        
        category_list =[category_1, category_2, category_3, category_4]
        db.session.add(category_list)
        
        print("🦸‍♀️ Seeding Products...")
        product_1 = Product(image ="image url for product 1", p_name = "Huddah lipstick 1", description = "A red lipstick", price = 200, category = category_1, brand = brand_1)
        product_2 = Product (image ="image url for product 2", p_name = "Rihanna mascara 1", description = "A red mascara", price = 100, category = category_2, brand = brand_2)

        product_list =[product_1, product_2]
        db.session.add(product_list)
        
        print("🦸‍♀️ Seeding Products...")
        
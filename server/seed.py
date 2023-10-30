from app import app, db
from models import User, Product, Brand, Category, Invoice, InvoiceProducts, Invoice, Role
from datetime import datetime
from sqlalchemy.orm import sessionmaker

with app.app_context():
    def delete_data():
    # this deletes existing db data in columns 
        print("🦸 Delete_data...")
        User.query.delete()
        Product.query.delete()
        Category.query.delete()
        Brand.query.delete()
        Invoice.query.delete()
        InvoiceProducts.query.delete()
        Role.query.delete()
    
    def seed_data():
        print("🦸‍♀️ Adding new data")
        
        print("🦸‍♀️ Seeding User Roles...")
        #role id 1 is equalt to admin and 2 is client
        admin_role = Role(name='Admin')
        db.session.add(admin_role)

        client_role = Role(name='Client')
        db.session.add(client_role)

        db.session.commit()

        print("🦸 Seeding Users...")
        user1 =User(first_name="kenya", last_name="kwanza", username = "yudiye", email="kenyakwanza@mail.com", ph_address = "Statehouse Road, Kilimani", password="kwisha2023", telephone = "254712345678", city_town = "Nairobi", role_id = 1)
        user2 =User(first_name="john", last_name="doe", username = "johndoe23", email="johndoe@mail.com", ph_address = "Muthurwa, Kamukunji", password="john2023", telephone = "254712345679", city_town = "Nairobi", role_id = 2)

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
        db.session.add_all(category_list)
        
        print("🦸‍♀️ Seeding Products...")
        product_1 = Product(image ="image url for product 1", p_name = "Huddah lipstick 1", description = "A red lipstick", price = 200, category = 1, brand = 1)
        product_2 = Product (image ="image url for product 2", p_name = "Rihanna mascara 1", description = "A red mascara", price = 100, category = 2, brand = 2)

        product_list =[product_1, product_2]
        db.session.add_all(product_list)
        
        print("🦸‍♀️ Seeding Invoices...")
        invoice_1 = Invoice( users = user1, products = product_1, quantity = 10, cost = 2000)
        invoice_2 = Invoice( users = user2, products = product_2, quantity = 10, cost = 1000)
        invoice_3 = Invoice( users = user2, products = product_2, quantity = 10, cost = 1000)



        invoice_list =[invoice_1, invoice_2, invoice_3]
        db.session.add_all(invoice_list)
        
        print("🦸‍♀️ Seeding Invoice_Products...")
        invoice_products_1 = InvoiceProducts(product_rl = product_1, invoice_rl = invoice_1)
        invoice_products_2 = InvoiceProducts(product_rl = product_1, invoice_rl = invoice_2)
        invoice_products_3 = InvoiceProducts(product_rl = product_1, invoice_rl = invoice_3)
        invoice_products_4 = InvoiceProducts(product_rl = product_2, invoice_rl = invoice_1)
        invoice_products_5 = InvoiceProducts(product_rl = product_2, invoice_rl = invoice_2)
        invoice_products_6 = InvoiceProducts(product_rl = product_2, invoice_rl = invoice_3)

        invoice_products_list =[invoice_products_1, invoice_products_2, invoice_products_3, invoice_products_4, invoice_products_5, invoice_products_6]   
        db.session.add_all(invoice_products_list)
        
        
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.app = app # bind the app to current SQLAlchemy instance
        delete_data()
        db.session.commit()
        seed_data()
        db.session.commit()
        
        print("🦸‍♀️ Done seeding!")

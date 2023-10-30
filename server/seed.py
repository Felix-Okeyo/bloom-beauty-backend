# from app import app, db
# from faker import Faker
# from models import User, Product, Brand, Category, Invoice, InvoiceProducts, Invoice
# from datetime import datetime
# from sqlalchemy.orm import sessionmaker

# fake = Faker()

# with app.app_context():
#     def delete_data():
#     # this deletes existing db data in columns 
#         print("🦸 Delete_data...")
#         User.query.delete()
#         Product.query.delete()
#         Category.query.delete()
#         Brand.query.delete()
#         Invoice.query.delete()
#         InvoiceProducts.query.delete()
        
    
#     def seed_data():
#         print("🦸 Seeding User data...")
#         user1 =User(first_name="kenya", last_name="kwanza", username = "yudiye", email="kenyakwanza@mail.com", ph_address = "Statehouse Road, Kilimani", password="kwisha2023", telephone = "254712345678", city_town = "Nairobi")
#         user2 =User(first_name="john", last_name="doe", username = "johndoe23", email="johndoe@mail.com", ph_address = "Muthurwa, Kamukunji", password="john2023", telephone = "254712345679", city_town = "Nairobi")

#         user_list =[user1, user2]
#         db.session.add_all(user_list)
    
#         print("🦸‍♀️ Seeding Brands...")
#         brand_1 = Brand(brand_name = "Huddah Cosmetics", brand_logo = "some url for her cosmetics logo here")
#         brand_2 = Brand(brand_name = "Rihanna", brand_logo = "Rihannas logo here")
        
#         brands_list = [brand_1, brand_2]
#         db.session.add_all(brands_list)
        
#         print("🦸‍♀️ Seeding Categories...")
#         category_1 = Category(cat_name = "Lipstick")
#         category_2 = Category(cat_name = "Face")
#         category_3 = Category(cat_name = "Eyes")
#         category_4 = Category(cat_name = "Make-up")
        
#         category_list =[category_1, category_2, category_3, category_4]
#         db.session.add_all(category_list)
        
#         print("🦸‍♀️ Seeding Products...")
#         product_1 = Product(image ="image url for product 1", p_name = "Huddah lipstick 1", description = "A red lipstick", price = 200, category = 1, brand = 1)
#         product_2 = Product (image ="image url for product 2", p_name = "Rihanna mascara 1", description = "A red mascara", price = 100, category = 2, brand = 2)

#         product_list =[product_1, product_2]
#         db.session.add_all(product_list)
        
#         print("🦸‍♀️ Seeding Invoices...")
#         invoice_1 = Invoice( users = user1, products = product_1, quantity = 10, cost = 2000)
#         invoice_2 = Invoice( users = user2, products = product_2, quantity = 10, cost = 1000)
#         invoice_3 = Invoice( users = user2, products = product_2, quantity = 10, cost = 1000)


#         invoice_list =[invoice_1, invoice_2, invoice_3]
#         db.session.add_all(invoice_list)
        
#         print("🦸‍♀️ Seeding Invoice_Products...")
#         invoice_products_1 = InvoiceProducts(product_rl = product_1, invoice_rl = invoice_1)
#         invoice_products_2 = InvoiceProducts(product_rl = product_1, invoice_rl = invoice_2)
#         invoice_products_3 = InvoiceProducts(product_rl = product_1, invoice_rl = invoice_3)
#         invoice_products_4 = InvoiceProducts(product_rl = product_2, invoice_rl = invoice_1)
#         invoice_products_5 = InvoiceProducts(product_rl = product_2, invoice_rl = invoice_2)
#         invoice_products_6 = InvoiceProducts(product_rl = product_2, invoice_rl = invoice_3)

#         invoice_products_list =[invoice_products_1, invoice_products_2, invoice_products_3, invoice_products_4, invoice_products_5, invoice_products_6]   
#         db.session.add_all(invoice_products_list)
        
        
#         db.session.commit()

# if __name__ == "__main__":
#     with app.app_context():
#         db.app = app # bind the app to current SQLAlchemy instance
#         delete_data()
#         db.session.commit()
#         seed_data()
#         db.session.commit()
        
#         print("🦸‍♀️ Done seeding!")


from app import app, db
from faker import Faker
from models import User, Product, Brand, Category, Invoice, InvoiceProducts, Invoice
from datetime import datetime
from sqlalchemy.orm import sessionmaker

fake = Faker()

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
        
    def seed_data():
        print("🦸 Seeding User data with Faker...")
        for _ in range(50):  # Generate 10 fake users
            user = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username=fake.user_name(),
                email=fake.email(),
                ph_address=fake.address(),
                password=fake.password(),
                telephone=fake.phone_number(),
                city_town=fake.city()
            )
            db.session.add(user)
    
        print("🦸‍♀️ Seeding Brands with Faker...")
        for _ in range(2):  # Generate 2 fake brands
            brand = Brand(
                brand_name=fake.company(),
                brand_logo=fake.url()
            )
            db.session.add(brand)
        
        print("🦸‍♀️ Seeding Categories with Faker...")
        for _ in range(4):  # Generate 4 fake categories
            category = Category(cat_name=fake.word())
            db.session.add(category)
        
        print("🦸‍♀️ Seeding Products with Faker...")
        for _ in range(2):  # Generate 2 fake products
            product = Product(
                image=fake.image_url(),
                p_name=fake.catch_phrase(),
                description=fake.text(),
                price=fake.random_int(min=10, max=1000),
                category=fake.random_int(min=1, max=4),  # Adjust to your category IDs
                brand=fake.random_int(min=1, max=2)  # Adjust to your brand IDs
            )
            db.session.add(product)
        
        print("🦸‍♀️ Seeding Invoices with Faker...")
        for _ in range(3):  # Generate 3 fake invoices
            user = User.query.order_by(User.id).first()
            product = Product.query.order_by(Product.id).first()
            invoice = Invoice(
                users=user,
                products=product,
                quantity=fake.random_int(min=1, max=20),
                cost=fake.random_int(min=10, max=5000)
            )
            db.session.add(invoice)
        
        print("🦸‍♀️ Seeding Invoice_Products with Faker...")
        products = Product.query.all()
        invoices = Invoice.query.all()
        for _ in range(6):  # Generate 6 fake invoice products
            product = fake.random_element(products)
            invoice = fake.random_element(invoices)
            invoice_product = InvoiceProducts(
                product_rl=product,
                invoice_rl=invoice
            )
            db.session.add(invoice_product)
        
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.app = app  # Bind the app to the current SQLAlchemy instance
        delete_data()
        db.session.commit()
        seed_data()
        db.session.commit()
        
        print("🦸‍♀️ Done seeding!")

from app import app, db
from faker import Faker
from models import User, Product, Brand, Category, Invoice, InvoiceProducts, Invoice, Role
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import random

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
        Role.query.delete()

    def seed_data():
        print("🦸‍♀️ Seeding User Roles...")
        admin_role = Role(name='Admin')
        db.session.add(admin_role)

        client_role = Role(name='Client')
        db.session.add(client_role)

        print("🦸‍♀️ Seeding Users with Faker...")
        admin = User(
                first_name= "John",
                last_name= "Messi",
                username="johnmessi",
                email="Johnmessi@example.com",
                ph_address="34, Woodley, Ngong-Road Nairobi",
                password=12345,
                telephone=fake.phone_number(),
                city_town=fake.city(),
                role_id = 1
            )
        db.session.add(admin)
        for _ in range(49):  # Generate 10 fake users
            clients = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username=fake.user_name(),
                email=fake.email(),
                ph_address=fake.address(),
                password=fake.password(),
                telephone=fake.phone_number(),
                city_town=fake.city(),
                role_id = 2
            )
           
            
            db.session.add(clients)
           

        print("🦸‍♀️ Seeding Brands with Faker...")
        for _ in range(5):  # Generate 2 fake brands
            brand = Brand(
                brand_name=fake.company(),
                brand_logo=fake.url()
            )
            db.session.add(brand)

        print("🦸‍♀️ Seeding Categories with Faker...")
        for _ in range(50):  # Generate 4 fake categories
            category = Category(cat_name=fake.word())
            db.session.add(category)

        print("🦸‍♀️ Seeding Products with Faker...")
        for _ in range(50):  # Generate 2 fake products
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
        for _ in range(50):  # Generate 3 fake invoices
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
        for _ in range(50):  # Generate 6 fake invoice products
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

        print(" 🦸‍♀️ Done seeding!")

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
        user1 = User(first_name="Kenya", last_name="Kwanza", username="yudiye", email="kenyakwanza@mail.com", ph_address="Statehouse Road, Kilimani", password="kwisha2023", telephone="254712345678", city_town="Nairobi", role_id=1)
        user2 = User(first_name="John", last_name="Doe", username="johndoe23", email="johndoe@mail.com", ph_address="Muthurwa, Kamukunji", password="john2023", telephone="254712345679", city_town="Nairobi", role_id=2)
        user3 = User(first_name="Alice", last_name="Smith", username="alicesmith", email="alice@mail.com", ph_address="123 Main St, Nairobi", password="alice123", telephone="254712345680", city_town="Nairobi", role_id=2)
        user4 = User(first_name="Bob", last_name="Johnson", username="bobjohnson", email="bob@mail.com", ph_address="456 Elm St, Nairobi", password="bob123", telephone="254712345681", city_town="Nairobi", role_id=2)

        user_list = [user1, user2, user3, user4]
        db.session.add_all(user_list)
    
        print("🦸‍♀️ Seeding Brands...")
        brand_1 = Brand(brand_name="Huddah Cosmetics", brand_logo="https://www.huddahstore.com/")
        brand_2 = Brand(brand_name="Rihanna", brand_logo="https://logowik.com/content/uploads/images/fenty-beauty9929.logowik.com.webp")
        brand_3 = Brand(brand_name="Maybelline", brand_logo="https://logos-world.net/maybelline-logo/")
        brand_4 = Brand(brand_name="MAC Cosmetics", brand_logo="https://1000logos.net/mac-cosmetics-logo/")

        brands_list = [brand_1, brand_2, brand_3, brand_4]
        db.session.add_all(brands_list)
        
        print("🦸‍♀️ Seeding Categories...")
        category_1 = Category(cat_name = "Lipstick")
        category_2 = Category(cat_name = "Face")
        category_3 = Category(cat_name = "Eyes")
        category_4 = Category(cat_name = "Make-up")
        
        category_list =[category_1, category_2, category_3, category_4]
        db.session.add_all(category_list)
        
        print("🦸‍♀️ Seeding Products...")
        product_1 = Product(image="https://www.pexels.com/photo/close-up-photo-of-person-holding-lipstick-3060257/", p_name="Huddah Lipstick - Red Velvet", description="High-quality red lipstick that provides a smooth and long-lasting finish. Perfect for any occasion.", price=200, category=category_1, brand=brand_1)
        product_2 = Product(image="https://www.pexels.com/photo/venus-mascara-2697787/", p_name="Rihanna Mascara - Volume Boost", description="Achieve voluminous lashes with Rihanna's mascara. This mascara lifts, separates, and adds volume for a dramatic look.", price=100, category=category_1, brand=brand_2)
        product_3 = Product(image="https://www.pexels.com/photo/makeup-palette-on-black-wooden-table-4620874/", p_name="Urban Chic Eyeshadow Palette", description="Explore a variety of shades with this eyeshadow palette. From subtle neutrals to bold colors, create endless eye looks.", price=250, category=category_3, brand=brand_1)
        product_4 = Product(image="https://www.pexels.com/photo/assorted-makeup-brush-set-7290669/", p_name="Luxury Makeup Brush Set", description="Upgrade your makeup routine with this luxurious brush set. The soft bristles and ergonomic handles ensure a flawless application.", price=150, category=category_4, brand=brand_2)
        product_5 = Product(image="https://www.pexels.com/photo/a-variety-of-lipglosses-on-a-pink-background-15854300/", p_name="Maybelline Lip Gloss - Pink Delight", description="Shiny and moisturizing lip gloss by Maybelline. Add a pop of color and shine to your lips with this Pink Delight shade.", price=120, category=category_1, brand=brand_3)
        product_6 = Product(image="https://www.pexels.com/photo/beauty-blush-brush-color-354962/", p_name="MAC Blush Brush", description="Sculpt and define your cheeks with this MAC blush brush. Soft and angled bristles make application easy and precise.", price=50, category=category_4, brand=brand_4)
        product_7 = Product(image="https://www.pexels.com/photo/close-up-photo-of-pink-lipstick-and-blush-on-2533266/", p_name="Maybelline Lipstick - Coral Crush", description="Vibrant coral lipstick by Maybelline. Provides a creamy texture and bold color payoff.", price=180, category=category_1, brand=brand_3)
        product_8 = Product(image="https://www.pexels.com/photo/studio-shot-of-foundation-in-glass-container-5403543/", p_name="MAC Foundation - Natural Glow", description="Lightweight foundation for a natural glow. Blends seamlessly and provides all-day coverage.", price=280, category=category_2, brand=brand_4)
        product_9 = Product(image="https://www.pexels.com/photo/skin-care-tools-set-photo-8015871/", p_name="Rihanna Face Cream - Hydrating Moisture", description="Hydrating face cream by Rihanna. Infused with moisturizing ingredients for soft and supple skin.", price=220, category=category_2, brand=brand_2)
        product_10 = Product(image="https://www.pexels.com/photo/powder-and-concealer-on-tray-7670761/", p_name="MAC Concealer - Full Coverage", description="Full coverage concealer by MAC. Conceals imperfections and brightens the under-eye area.", price=150, category=category_2, brand=brand_4)
        product_11 = Product(image="https://www.pexels.com/photo/assorted-colors-of-eye-shadow-palette-7290741/", p_name="Maybelline Eyeshadow Palette - Bold Hues", description="Dive into a world of bold hues with this Maybelline eyeshadow palette. Create vibrant and daring eye looks with a mix of matte and shimmer shades.", price=280, category=category_3, brand=brand_3)
        product_12 = Product(image="https://www.pexels.com/photo/makeup-brush-on-black-container-1115128/", p_name="Huddah Makeup Brush Set", description="High-quality makeup brush set by Huddah Cosmetics. Includes brushes for eyes, face, and lips.", price=200, category=category_4, brand=brand_1)

        product_list = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9, product_10, product_11, product_12]
        db.session.add_all(product_list)
        
        print("🦸‍♀️ Seeding Invoices...")
        invoice_1 = Invoice(users=user1, products=product_1, quantity=10, cost=2000)
        invoice_2 = Invoice(users=user2, products=product_2, quantity=10, cost=1000)
        invoice_3 = Invoice(users=user3, products=product_3, quantity=5, cost=1250)
        invoice_4 = Invoice(users=user4, products=product_4, quantity=8, cost=1200)
        invoice_5 = Invoice(users=user1, products=product_5, quantity=12, cost=1440)
        invoice_6 = Invoice(users=user2, products=product_6, quantity=15, cost=750)
        invoice_7 = Invoice(users=user3, products=product_7, quantity=7, cost=1260)
        invoice_8 = Invoice(users=user4, products=product_8, quantity=6, cost=1680)
        invoice_9 = Invoice(users=user1, products=product_9, quantity=9, cost=1980)
        invoice_10 = Invoice(users=user2, products=product_10, quantity=11, cost=1650)
        invoice_11 = Invoice(users=user3, products=product_11, quantity=14, cost=3920)
        invoice_12 = Invoice(users=user4, products=product_12, quantity=20, cost=4000)

        invoice_list = [invoice_1, invoice_2, invoice_3, invoice_4, invoice_5, invoice_6, invoice_7, invoice_8, invoice_9, invoice_10, invoice_11, invoice_12]
        db.session.add_all(invoice_list)
        
        print("🦸‍♀️ Seeding Invoice_Products...")
        invoice_products_1 = InvoiceProducts(product_rl=product_1, invoice_rl=invoice_1)
        invoice_products_2 = InvoiceProducts(product_rl=product_2, invoice_rl=invoice_2)
        invoice_products_3 = InvoiceProducts(product_rl=product_3, invoice_rl=invoice_3)
        invoice_products_4 = InvoiceProducts(product_rl=product_4, invoice_rl=invoice_4)
        invoice_products_5 = InvoiceProducts(product_rl=product_5, invoice_rl=invoice_5)
        invoice_products_6 = InvoiceProducts(product_rl=product_6, invoice_rl=invoice_6)
        invoice_products_7 = InvoiceProducts(product_rl=product_7, invoice_rl=invoice_7)
        invoice_products_8 = InvoiceProducts(product_rl=product_8, invoice_rl=invoice_8)
        invoice_products_9 = InvoiceProducts(product_rl=product_9, invoice_rl=invoice_9)
        invoice_products_10 = InvoiceProducts(product_rl=product_10, invoice_rl=invoice_10)
        invoice_products_11 = InvoiceProducts(product_rl=product_11, invoice_rl=invoice_11)
        invoice_products_12 = InvoiceProducts(product_rl=product_12, invoice_rl=invoice_12)

        invoice_products_list = [invoice_products_1, invoice_products_2, invoice_products_3, invoice_products_4, invoice_products_5, invoice_products_6, invoice_products_7, invoice_products_8, invoice_products_9, invoice_products_10, invoice_products_11, invoice_products_12]
        db.session.add_all(invoice_products_list)

        db.session.commit()

if __name__  == "_main_":
    with app.app_context():
        db.app = app # bind the app to current SQLAlchemy instance
        delete_data()
        db.session.commit()
        seed_data()
        db.session.commit()
        
        print("🦸‍♀️ Done seeding!")
import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_app.settings')
django.setup()

from products.models import Category, Product
from django.utils.text import slugify
import urllib.request
from django.core.files.base import ContentFile

def seed_data():
    print("Clearing existing data...")
    Product.objects.all().delete()
    Category.objects.all().delete()

    categories = [
        "Electronics", "Fashion", "Home & Living", "Beauty", "Sports"
    ]
    
    cat_objs = []
    for cat_name in categories:
        cat = Category.objects.create(name=cat_name)
        cat_objs.append(cat)
        print(f"Created Category: {cat_name}")

    products_data = [
        {"name": "UltraBook Pro 14", "category": "Electronics", "price": 1299.99, "discount_price": 1199.99, "stock": 15},
        {"name": "Wireless Noise Cancelling Headphones", "category": "Electronics", "price": 299.99, "discount_price": None, "stock": 40},
        {"name": "Smart Watch Series 9", "category": "Electronics", "price": 399.99, "discount_price": 349.99, "stock": 25},
        
        {"name": "Premium Cotton T-Shirt", "category": "Fashion", "price": 29.99, "discount_price": None, "stock": 100},
        {"name": "Slim Fit Denim Jacket", "category": "Fashion", "price": 89.99, "discount_price": 69.99, "stock": 30},
        {"name": "Classic Leather Boots", "category": "Fashion", "price": 149.99, "discount_price": None, "stock": 20},
        
        {"name": "Minimalist Coffee Table", "category": "Home & Living", "price": 199.99, "discount_price": 179.99, "stock": 10},
        {"name": "Ergonomic Office Chair", "category": "Home & Living", "price": 249.99, "discount_price": None, "stock": 8},
        {"name": "Velvet Throw Pillow", "category": "Home & Living", "price": 24.99, "discount_price": None, "stock": 50},
        
        {"name": "Hydrating Facial Serum", "category": "Beauty", "price": 45.00, "discount_price": 39.99, "stock": 60},
        {"name": "Organic Matte Lipstick", "category": "Beauty", "price": 18.00, "discount_price": None, "stock": 120},
        
        {"name": "Yoga Mat Premium", "category": "Sports", "price": 55.00, "discount_price": None, "stock": 25},
        {"name": "Dumbbell Set (5kg x 2)", "category": "Sports", "price": 35.00, "discount_price": 29.99, "stock": 15},
    ]

    for p_data in products_data:
        cat = Category.objects.get(name=p_data["category"])
        product = Product.objects.create(
            category=cat,
            name=p_data["name"],
            price=p_data["price"],
            discount_price=p_data["discount_price"],
            stock=p_data["stock"],
            description=f"This is a premium {p_data['name']} from our {p_data['category']} collection.",
            is_available=True
        )
        
        print(f"Fetching image for {p_data['name']}...")
        image_url = f"https://picsum.photos/600/400?random={random.randint(1, 10000)}"
        try:
            req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            product.image.save(f"{slugify(p_data['name'])}.jpg", ContentFile(response.read()), save=True)
        except Exception as e:
            print(f"Failed to fetch image for {p_data['name']}: {e}")
            
        print(f"Created Product: {p_data['name']}")

    print("Seeding complete!")

if __name__ == "__main__":
    seed_data()

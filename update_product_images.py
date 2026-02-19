import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_app.settings')
django.setup()

from products.models import Product

def update_images():
    image_map = {
        "UltraBook Pro 14": "products/laptop.jpg",
        "Wireless Noise Cancelling Headphones": "products/headphones.jpg",
        "Smart Watch Series 9": "products/smartwatch.jpg",
        "Premium Cotton T-Shirt": "products/tshirt.jpg",
        "Slim Fit Denim Jacket": "products/jacket.jpg",
        "Classic Leather Boots": "products/boots.jpg",
        "Minimalist Coffee Table": "products/table.jpg",
        "Ergonomic Office Chair": "products/chair.jpg",
        "Velvet Throw Pillow": "products/table.jpg", # reusing table or something
        "Hydrating Facial Serum": "products/serum.jpg",
        "Organic Matte Lipstick": "products/lipstick.jpg",
        "Yoga Mat Premium": "products/yogamat.jpg",
        "Dumbbell Set (5kg x 2)": "products/dumbbells.jpg",
    }

    for p_name, img_path in image_map.items():
        try:
            p = Product.objects.get(name=p_name)
            p.image = img_path
            p.save()
            print(f"Updated image for: {p_name}")
        except Product.DoesNotExist:
            print(f"Product not found: {p_name}")

    print("Image update complete!")

if __name__ == "__main__":
    update_images()

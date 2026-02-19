from .models import Cart, CartItem
from products.models import Product
from django.core.exceptions import ValidationError

class OutOfStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class CartManager:
    """Service class for Cart operations (Refined for specific requirements)"""
    
    def __init__(self, user=None):
        self.user = user
        self.cart = self._get_or_create_cart()

    def _get_or_create_cart(self):
        if self.user and self.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=self.user)
            return cart
        return None

    def add_to_cart(self, product_id, quantity=1):
        try:
            product = Product.objects.get(id=product_id)
            if product.stock < quantity:
                raise OutOfStockError(f"Only {product.stock} items left in stock.")
            
            if quantity <= 0:
                raise InvalidQuantityError("Quantity must be at least 1.")

            cart_item, created = CartItem.objects.get_or_create(cart=self.cart, product=product)
            if not created:
                if product.stock < cart_item.quantity + quantity:
                    raise OutOfStockError(f"Cannot add more. Only {product.stock} items available.")
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            
            cart_item.save()
            return cart_item
        except Product.DoesNotExist:
            raise ValidationError("Product not found.")

    def update_quantity(self, item_id, quantity):
        try:
            item = CartItem.objects.get(id=item_id, cart=self.cart)
            if item.product.stock < quantity:
                raise OutOfStockError(f"Only {item.product.stock} items available.")
            
            if quantity <= 0:
                item.delete()
                return None
            
            item.quantity = quantity
            item.save()
            return item
        except CartItem.DoesNotExist:
            raise ValidationError("Item not found in cart.")

    def remove_item(self, item_id):
        CartItem.objects.filter(id=item_id, cart=self.cart).delete()

    def calculate_total(self):
        return sum(item.total_price for item in self.cart.items.all())

    def clear(self):
        self.cart.items.all().delete()

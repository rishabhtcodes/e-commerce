import random
import uuid
from .models import Order, OrderItem, Payment
from cart.services import CartManager
from django.db import transaction

class PaymentService:
    @staticmethod
    def process_payment(order):
        """Structured Payment Service"""
        # Simulate dummy logic
        success = random.random() < 0.9
        transaction_id = str(uuid.uuid4())
        
        payment = Payment.objects.create(
            order=order,
            transaction_id=transaction_id,
            amount=order.total_amount,
            status='Success' if success else 'Failed'
        )
        return payment

class CheckoutService:
    @staticmethod
    def process_checkout(user):
        cart_manager = CartManager(user)
        cart = cart_manager.cart
        
        if not cart.items.exists():
            return None, "Cart is empty."

        try:
            with transaction.atomic():
                # 1. Create Order
                order = Order.objects.create(
                    user=user,
                    total_amount=cart_manager.calculate_total(),
                    status='Pending'
                )

                # 2. Create Order Items and Update Stock
                for item in cart.items.all():
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        price=item.product.discount_price or item.product.price,
                        quantity=item.quantity
                    )
                    # Update stock
                    item.product.stock -= item.quantity
                    item.product.save()

                # 3. Process Payment via PaymentService
                payment = PaymentService.process_payment(order)
                
                if payment.status == 'Success':
                    # 4. Clear Cart
                    cart_manager.clear()
                    return order, "Order placed and payment successful."
                else:
                    # In a real app, we might keep the order pending but mark payment failed
                    order.status = 'Cancelled'
                    order.save()
                    return None, "Payment failed. Order cancelled."
                    
        except Exception as e:
            return None, f"An error occurred: {str(e)}"

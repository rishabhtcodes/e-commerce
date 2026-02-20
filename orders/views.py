from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.services import CartManager
from accounts.email_service import EmailService

@login_required
def checkout(request):
    cart_manager = CartManager(request.user)
    if not cart_manager.cart or cart_manager.cart.items.count() == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect('cart:cart_detail')
        
    if request.method == 'POST':
        # Create the order
        order = Order.objects.create(
            user=request.user,
            total_amount=cart_manager.calculate_total(),
            status='Pending'
        )
        
        # Move cart items to order items
        for item in cart_manager.cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.discount_price if item.product.discount_price else item.product.price,
                quantity=item.quantity
            )
            
        # Clear the cart
        cart_manager.cart.items.all().delete()

        # Send order confirmation email
        EmailService.send_order_confirmation(request.user, order)

        messages.success(request, "Order placed successfully! Check your email for confirmation.")
        return redirect('orders:success', order_id=order.id)
        
    return render(request, 'orders/checkout.html', {
        'cart': cart_manager.cart,
        'total_price': cart_manager.calculate_total()
    })

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/success.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})

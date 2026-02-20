from .services import CartManager

def cart_processor(request):
    cart_count = 0
    if request.user.is_authenticated:
        try:
            cart_manager = CartManager(request.user)
            if cart_manager.cart:
                cart_count = sum(item.quantity for item in cart_manager.cart.items.all())
        except Exception:
            pass
    return {'cart_count': cart_count}

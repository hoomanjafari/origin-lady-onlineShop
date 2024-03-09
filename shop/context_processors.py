from .models import AddCart
from .cart import Cart


def cart_detail(request):
    if request.user.is_authenticated:
        cart_items = AddCart.objects.filter(customer=request.user)
        quantity = 0
        total_price = 0
        for i in cart_items:
            quantity += int(i.selected_quantity)
            total_price += int(i.total_price)
        return {'cart_items': cart_items, 'cart_items_count': quantity, 'total_price': total_price}
    else:
        cart_items = AddCart.objects.filter(guest_session_id=request.session.session_key)
        quantity = 0
        total_price = 0
        for i in cart_items:
            quantity += int(i.selected_quantity)
            total_price += int(i.total_price)
        return {'cart_items': cart_items, 'cart_items_count': quantity, 'total_price': total_price}


def cart(request):
    return {'cart': Cart(request)}

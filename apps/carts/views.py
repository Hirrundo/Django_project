from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from apps.catalog.models import Dish
from .models import Cart, CartItem

@login_required
def add_to_cart_view(request, dish_id):
    if request.method != 'POST':
        return redirect('catalog:dish_list')
    dish = get_object_or_404(Dish, id=dish_id, is_available=True)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        dish=dish,
        defaults={'quantity': 1},
)
    if not created:
        item.quantity += 1
        item.save()
        messages.success(request, f'«{dish.name}» — теперь {item.quantity} шт.')
    else:
        messages.success(request, f'«{dish.name}» добавлено в корзину.')
    return redirect('catalog:dish_detail', slug=dish.slug)
@login_required
def cart_detail_view(request):

    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = (
        cart.items
        .select_related('dish', 'dish__category')
        .all()
    )
    context = {
        'cart': cart,
        'items': items,
    }
    return render(request, 'carts/cart_detail.html', context)
# Create your views here.

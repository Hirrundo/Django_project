from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.carts.models import Cart
from .forms import OrderForm
from .models import Order
from .services import create_order_from_cart
from django.views.decorators.http import require_POST

@login_required
def order_create_view(request):

    cart = Cart.objects.get_or_create(user=request.user)[0]
    if not cart.items.exists():
        messages.warning(request, 'Корзина пуста — нечего оформлять.')
        return redirect('carts:detail')
    if request.method == 'POST':

        form = OrderForm(request.POST)
        if form.is_valid():
            order = create_order_from_cart(cart, **form.cleaned_data)
            messages.success(request, f'Заказ No{order.pk} принят!')
            return redirect('orders:detail', pk=order.pk)
    else:

        initial = {
            'address': request.user.profile.address,
            'phone': request.user.profile.phone,
        }
        form = OrderForm(initial=initial)
    return render(request, 'orders/order_form.html', {
                            'form': form,
                            'cart': cart,
            })
@login_required
def order_detail_view(request, pk):

    order = get_object_or_404(
        Order.objects
        .select_related('user', 'courier')
        .prefetch_related('items__dish'),
        pk=pk,
        user=request.user, # ← защита: только свои
    )
    return render(request, 'orders/order_detail.html', {'order': order})
@login_required
def order_list_view(request):

    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related('items')
        .order_by('-created_at')
    )
    return render(request, 'orders/order_list.html', {'orders': orders})
@login_required
@require_POST
def order_cancel_view(request, pk):

    order = get_object_or_404(Order, pk=pk, user=request.user)
    if not order.can_be_cancelled():
        messages.error(request, 'Этот заказ уже нельзя отменить.')
        return redirect('orders:detail', pk=order.pk)
    order.status = Order.STATUS_CANCELLED
    order.save(update_fields=['status'])
    messages.info(request, f'Заказ No{order.pk} отменён.')
    return redirect('orders:detail', pk=order.pk)
# Create your views here.

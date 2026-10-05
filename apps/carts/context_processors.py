def cart_count(request):
    if request.user.is_authenticated:
        try:
            count = request.user.cart.item_count
        except Exception:
            count = 0
    else:
        count = 0
    return {'cart_count': count}
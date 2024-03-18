from django.shortcuts import render
from .models import Orders, OrderItem
from . import forms
from urllib.parse import unquote
import json
def order(request):
    form = forms.OrderForm(request.POST or None)
    cookieProducts = request.COOKIES.get('korzinka')
    if request.method == "POST" and cookieProducts is not None:
        address = request.POST.get('address')
        user_id = request.user.id
        order_data = Orders.objects.create(address=address, user_id=user_id)
        print(order_data.id)
        items1 = unquote(cookieProducts)
        items = json.loads(items1)
        for item in items:
            order_items = OrderItem.objects.create(product_id=item['id'], count=item['quantity'], order_id=order_data.id)
            print(order_items)
    ctx = {
        "form": form
    }
    return render(request, "order.html", ctx)

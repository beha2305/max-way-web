from django.shortcuts import render
from .models import Orders

def order(request):
    return render(request, "order.html", {})

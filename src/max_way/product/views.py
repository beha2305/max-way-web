from django.shortcuts import render
from .models import Category
from . import services

def index(request):
    products = services.get_products()
    categories = Category.objects.all()

    ctx = {
        "products": products,
        "categories": categories
    }

    return render(request, "index.html", ctx)

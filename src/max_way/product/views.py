from django.shortcuts import render
from .models import Category
from . import services

def index(request):
    category_id = request.GET.get("category")
    products = services.get_products(category_id=category_id)
    categories = Category.objects.all()

    print(category_id)
    ctx = {
        "products": products,
        "categories": categories
    }

    return render(request, "index.html", ctx)

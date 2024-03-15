from django.shortcuts import render
from .models import Category
from . import services

def index(request):
    categories = Category.objects.prefetch_related('product_set').all()

    ctx = {
        "categories": categories
    }
    return render(request, "index.html", ctx)

from django.shortcuts import render
from .models import Category, Product
from . import services
from urllib.parse import unquote
import json
def index(request):
    categories = Category.objects.prefetch_related('product_set').all()

    ctx = {
        "categories": categories
    }
    return render(request, "index.html", ctx)
def bucket(request):
    cookieProducts = request.COOKIES.get('korzinka')
    items1 = unquote(cookieProducts)
    items = json.loads(items1)
    print(items)
    products = Product.objects.filter(id__in=[item['id'] for item in items])
    # print(products)
    ctx = {
        "product": products
    }
    return render(request, 'korzinka.html', ctx)
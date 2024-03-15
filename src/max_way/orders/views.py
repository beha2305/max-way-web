from django.shortcuts import render
from .models import Orders
from . import forms

def order(request):
    form = forms.OrderForm(request.POST or None)
    print(request.method,form, form.is_valid(), '-----------')
    if request.method == "POST":
        # form.save()
        print(form, form.is_valid())
    ctx = {
        "form" : form
    }
    return render(request, "order.html", ctx)

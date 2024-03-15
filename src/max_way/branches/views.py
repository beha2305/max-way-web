from django.shortcuts import render
from .models import Branches
def branches(request):
    branches = Branches.objects.all()
    ctx = {
        "branches": branches
    }
    return render(request, 'branches.html', ctx)
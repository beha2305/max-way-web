from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as loginUser
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        print(form, form.is_valid())
        form.save()
        return redirect('login')

    ctx = {
        'form': form
    }
    return render(request, 'register.html', ctx)

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('index')

    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)
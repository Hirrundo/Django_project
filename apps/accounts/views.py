from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # сразу логиним
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('catalog:dish_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog:dish_list')
    else:
        messages.error(request, 'Неверный логин или пароль')
    return render(request, 'registration/login.html')
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'users/home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'users/register.html', {'error': "Passwords don't match"})

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('login')
    
    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Check if user is admin/staff
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'users/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')

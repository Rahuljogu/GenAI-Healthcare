
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from ai_assistant.models import ChatLog

def is_admin(user):
    return user.is_authenticated and user.is_staff

def admin_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, "admin_panel/login.html", {"error": "Invalid admin credentials"})
    return render(request, "admin_panel/login.html")

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "admin_panel/dashboard.html")

@login_required
@user_passes_test(is_admin)
def user_management(request):
    users = User.objects.exclude(is_superuser=True)
    return render(request, "admin_panel/user_management.html", {"users": users})

@login_required
@user_passes_test(is_admin)
def chat_management(request):
    chats = ChatLog.objects.select_related("user").order_by("-timestamp")
    return render(request, "admin_panel/chat_management.html", {"chats": chats})

def admin_logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from ai_assistant.models import ChatLog
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

# --- Edit User ---
@login_required
@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.is_active = bool(request.POST.get('is_active'))
        user.save()
        return redirect('user_management')
    return render(request, "admin_panel/edit_user.html", {"user_obj": user})

# --- Delete User ---
@login_required
@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_management')

# --- Delete Chat ---
@login_required
@user_passes_test(is_admin)
def delete_chat(request, chat_id):
    chat = get_object_or_404(ChatLog, id=chat_id)
    chat.delete()
    return redirect('chat_management')

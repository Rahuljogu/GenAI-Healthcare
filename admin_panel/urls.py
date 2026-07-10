from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.user_management, name='user_management'),
    path('chats/', views.chat_management, name='chat_management'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
path('chats/delete/<int:chat_id>/', views.delete_chat, name='delete_chat'),

]

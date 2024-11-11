from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('add_entry/', views.add_entry, name='add_entry'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
     path('logout/', views.user_logout, name='logout'),
]

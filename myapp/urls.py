from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_entry, name='add_entry'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
]

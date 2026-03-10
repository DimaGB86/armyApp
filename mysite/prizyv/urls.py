# prizyv/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.priziv_index, name='priziv_index'),  # Только главная страница
    # Удалены маршруты add_prizivnik и edit_prizivnik
]
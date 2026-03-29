from django.urls import path
from . import views

urlpatterns = [
    path('', views.priziv_index, name='priziv_index'),
]
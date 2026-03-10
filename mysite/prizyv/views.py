# prizyv/views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Prizivnik

def priziv_index(request: HttpRequest):
    """Главная страница с формой для призывников"""
    
    if request.method == 'POST':
        # Получаем данные из формы
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        patronymic = request.POST.get('patronymic', '')
        phone = request.POST.get('phone')
        city = request.POST.get('city', '')
        
        # Создаем запись в базе данных
        Prizivnik.objects.create(
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
            phone=phone,
            address=city,
        )
        
        # Перенаправляем на страницу успеха
        return render(request, 'prizyv/success.html')
    
    # GET запрос - показываем страницу с формой
    return render(request, 'prizyv/priziv-index.html')
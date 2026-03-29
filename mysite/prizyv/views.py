from django.shortcuts import render, redirect
from .models import Application

def priziv_index(request):
    """Главная страница с формой для призывников"""
    
    if request.method == 'POST':
        # Получаем данные из формы
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        patronymic = request.POST.get('patronymic', '')
        phone = request.POST.get('phone')
        city = request.POST.get('city', '')
        
        # Создаем запись в базе данных
        Application.objects.create(
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
            phone=phone,
            city=city,
        )
        
        # Перенаправляем на страницу успеха
        return render(request, 'prizyv/success.html')
    
    # GET запрос - показываем страницу с формой
    return render(request, 'prizyv/priziv-index.html')
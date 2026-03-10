# prizyv/admin.py
from django.contrib import admin
from .models import Prizivnik, Application

@admin.register(Prizivnik)
class PrizivnikAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'phone', 'created_at')
    search_fields = ('last_name', 'first_name', 'phone')
    list_filter = ('created_at',)

@admin.register(Application)  # Добавляем регистрацию модели заявок
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'city', 'created_at')
    search_fields = ('last_name', 'first_name', 'phone')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)  # Дата создания только для чтения
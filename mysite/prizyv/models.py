# prizyv/models.py
from django.db import models

class Prizivnik(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100, blank=True)
    phone = models.CharField('Телефон', max_length=20)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    address = models.TextField('Адрес', blank=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Призывник'
        verbose_name_plural = 'Призывники'
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}".strip()

class Application(models.Model):
    """Заявки с главной страницы"""
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100, blank=True)
    phone = models.CharField('Телефон', max_length=20)
    city = models.CharField('Город', max_length=100, blank=True)
    created_at = models.DateTimeField('Дата заявки', auto_now_add=True)
    
    # Поля с датой и временем сделаем необязательными или удалим
    # appointment_date = models.DateField('Желаемая дата', null=True, blank=True)
    # appointment_time = models.TimeField('Желаемое время', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.phone}"
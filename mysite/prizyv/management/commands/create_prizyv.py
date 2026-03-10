# create_prizivniki.py
import os
import django
from datetime import date, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from prizyv.models import Prizivnik

# Тестовые данные призывников
test_prizivniki = [
    {
        'fio': 'Иванов Иван Иванович',
        'phone': '+7 (999) 123-45-67',
        'birth_date': date(2000, 5, 15),
        'address': 'г. Москва, ул. Ленина, д. 10, кв. 5'
    },
    {
        'fio': 'Петров Петр Петрович',
        'phone': '+7 (999) 234-56-78',
        'birth_date': date(2001, 3, 20),
        'address': 'г. Санкт-Петербург, ул. Невский пр., д. 25, кв. 12'
    },
    {
        'fio': 'Сидоров Сидор Сидорович',
        'phone': '+7 (999) 345-67-89',
        'birth_date': date(2000, 11, 8),
        'address': 'г. Екатеринбург, ул. Мира, д. 5, кв. 30'
    },
    {
        'fio': 'Кузнецов Андрей Сергеевич',
        'phone': '+7 (999) 456-78-90',
        'birth_date': date(2002, 7, 12),
        'address': 'г. Новосибирск, ул. Красный пр., д. 15, кв. 7'
    },
    {
        'fio': 'Смирнов Алексей Николаевич',
        'phone': '+7 (999) 567-89-01',
        'birth_date': date(2001, 9, 25),
        'address': 'г. Казань, ул. Баумана, д. 30, кв. 4'
    },
]

# Очищаем существующие данные (опционально)
# Prizivnik.objects.all().delete()

# Создаем новых призывников
for data in test_prizivniki:
    Prizivnik.objects.create(**data)

print(f"✅ Создано {len(test_prizivniki)} призывников")

# Показываем созданные записи
print("\nСписок созданных призывников:")
for p in Prizivnik.objects.all():
    print(f"  - {p.fio}: {p.phone} ({p.birth_date})")
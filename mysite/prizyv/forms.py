# prizyv/forms.py
from django import forms
from .models import Prizivnik

class PrizivnikModelForm(forms.ModelForm):
    class Meta:
        model = Prizivnik
        fields = ['last_name', 'first_name', 'patronymic', 'phone', 'birth_date', 'address']
        
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'patronymic': 'Отчество',
            'phone': 'Телефон',
            'birth_date': 'Дата рождения',
            'address': 'Адрес',
        }
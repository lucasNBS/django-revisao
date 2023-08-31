from django.forms import ModelForm
from django import forms
from .models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'input'}),
            'nome_empresa': forms.TextInput(attrs={'class': 'input'}),
            'categoria_empresa': forms.TextInput(attrs={'class': 'input'}),
            'quitado': forms.CheckboxInput(attrs={'class': 'check'}),
            'stand': forms.Select(attrs={'class': 'input'}),
        }
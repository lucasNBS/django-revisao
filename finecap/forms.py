from django.forms import ModelForm
from django import forms
from .models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        models = Reserva
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(),
            'nome_empresa': forms.TextInput(),
            'categoria_empresa': forms.TextInput(),
            'quitado': forms.CheckboxInput(),
            'stand': forms.Select(),
        }
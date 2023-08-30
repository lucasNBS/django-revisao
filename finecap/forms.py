from django import forms
from .models import Reserva, Stand

class ReservaForms(forms.ModelForm):
    class Meta:
        models = Reserva
        fields = '__all__'

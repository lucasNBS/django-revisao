from django.contrib import admin
from .models import Reserva, Stand

# Register your models here.
@admin.register(Reserva)
class ReservaAadmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nome_empresa', 'categoria_empresa', 'quitado', 'stand')

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'valor')
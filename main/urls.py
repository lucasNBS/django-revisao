"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finecap.views import reservas, reserva, reserva_criar, reserva_editar, reserva_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', reservas, name='reservas'),
    path('reserva/<int:id>', reserva, name='reserva'),
    path('reservas/criar', reserva_criar, name='reservas-criar'),
    path('reservas/editar/<int:id>', reserva_editar, name='reservas-editar'),
    path('reservas/remover/<int:id>', reserva_remover, name='reservas-remover'),
]

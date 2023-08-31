from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.
def reservas(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas': reservas
    }
    return render(request, 'finecap/reservas.html', context)

def reserva(request, id=id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {
        'reserva': reserva
    }
    return render(request, 'finecap/reserva.html', context)

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
    else:
        form = ReservaForm()

    return render(request, 'finecap/formulario.html', { 'form': form })

def reserva_remover(request, id=id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reservas')

def reserva_editar(request, id=id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'finecap/formulario.html', { 'form': form })

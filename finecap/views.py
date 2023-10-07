from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Reserva
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/account/login')
def reservas(request):
    reservas = Reserva.objects.all().order_by('data')

    paginator = Paginator(reservas, 1)
    pagina = request.GET.get("pagina")
    pag_obj = paginator.get_page(pagina)

    name = request.GET.get("nome")
    quitado = request.GET.get("quitado")
    valor = request.GET.get("valor")
    data = request.GET.get("data")

    if name:
        reservas = reservas.filter(nome_empresa__icontains=name)
    if quitado is not None:
        reservas = reservas.filter(quitado=str(quitado))
    if valor:
        reservas = reservas.filter(valor=valor)
    if data:
        reservas = reservas.filter(data__gte=data)

    context = {
        'reservas': reservas,
        'pag_obj': pag_obj
    }

    return render(request, 'finecap/reservas.html', context)

@login_required(login_url='/account/login')
def reserva(request, id=id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {
        'reserva': reserva
    }
    return render(request, 'finecap/reserva.html', context)

@login_required(login_url='/account/login')
def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
    else:
        form = ReservaForm()

    return render(request, 'finecap/formulario.html', { 'form': form })

@login_required(login_url='/account/login')
def reserva_remover(request, id=id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reservas')

@login_required(login_url='/account/login')
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

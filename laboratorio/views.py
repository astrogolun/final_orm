from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm
# Create your views here.


# Crear Laboratorio
def insertar_lab(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_lab')  
    else:
        form = LaboratorioForm()

    return render(request, 'insertar.html', {'form': form})


# Obtener los Laboratorios
def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'mostrar.html', {'laboratorios': laboratorios})
    
# Editar Laboratorio
def editar_lab(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('mostrar_lab')

    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'editar.html', {'form': form})

# Eliminar Laboratorio
def eliminar_lab(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar_lab')

    return render(request, 'eliminar.html', {'laboratorio': laboratorio})







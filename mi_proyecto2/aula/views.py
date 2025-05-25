from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaForm
from .models import Nota

def agregar_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_notas')
    return render(request, 'aula/formulario.html', {'form': form, 'titulo': 'Agregar Alumno'})

def agregar_curso(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_notas')
    return render(request, 'aula/formulario.html', {'form': form, 'titulo': 'Agregar Curso'})

def agregar_nota(request):
    form = NotaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_notas')
    return render(request, 'aula/formulario.html', {'form': form, 'titulo': 'Agregar Nota'})

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'aula/lista_notas.html', {'notas': notas})
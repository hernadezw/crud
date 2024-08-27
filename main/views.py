from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.safestring import mark_safe
from .forms import ProfesorForm, CursoForm, AlumnoForm, NotaForm
from .models import Profesor, Curso, Alumno, Nota

@login_required  #decoradores
def dashboard(request):
    return render(request, 'dashboard.html')

# Vista para crear profesor
def create_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfesorForm()
    return render(request, 'create_profesor.html', {'form': form})








# Vista para crear curso
def create_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CursoForm()
    return render(request, 'create_curso.html', {'form': form})

# Vista para crear alumno
def create_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AlumnoForm()
    return render(request, 'create_alumno.html', {'form': form})

# Vista para crear nota
def create_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NotaForm()
    return render(request, 'create_nota.html', {'form': form})


















def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 
                mark_safe(f'Account created successfully for {username}! <a href="/">Login here</a>')
            )
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
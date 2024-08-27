from django import forms
from .models import Profesor, Curso, Alumno, Nota

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'especialidad']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'profesor']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'cursos']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['alumno', 'curso', 'nota']
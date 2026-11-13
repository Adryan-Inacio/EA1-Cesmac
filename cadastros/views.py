from django.shortcuts import render
from .models import Aluno, Curso

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos': alunos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})
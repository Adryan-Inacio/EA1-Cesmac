from django.contrib import admin
from .models import Aluno, Curso

class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('alunos',)

admin.site.register(Aluno)
admin.site.register(Curso, CursoAdmin)
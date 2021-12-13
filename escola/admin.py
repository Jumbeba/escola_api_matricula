from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    # Configurações do admin dos alunos
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    # Configurações do admin dos cursos
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)


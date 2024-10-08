from django.contrib import admin
from .models import Funcionario, Cliente, Veiculo, Entrada, Saida


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','numero_identificacao', 'CPF', 'telefone', 'email', 'turno', 'salario', 'foto')
    
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CPF', 'telefone', 'email')
    
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'cor', 'tipo', 'cliente')
    
@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'funcionario', 'dataHora')


@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'funcionario', 'dataHora')


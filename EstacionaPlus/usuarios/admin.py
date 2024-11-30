from django.contrib import admin
from .models import VeiculoSet, EntradaSet, SaidaSet

class EntradaSetAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'usuario', 'data_entrada', 'hora_entrada')
    ordering = ('data_entrada', 'hora_entrada')
    list_filter = ('data_entrada', 'usuario')  

class SaidaSetAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'usuario', 'data_saida', 'hora_saida')  
    ordering = ('data_saida', 'hora_saida')
    list_filter = ('data_saida', 'usuario') 

class VeiculoSetAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'modelo', 'tipo_veiculo', 'placa', 'publico')
    ordering = ('cliente', 'modelo')
    list_filter = ('tipo_veiculo', 'publico', 'cliente')

admin.site.register(VeiculoSet, VeiculoSetAdmin)
admin.site.register(EntradaSet, EntradaSetAdmin)
admin.site.register(SaidaSet, SaidaSetAdmin)

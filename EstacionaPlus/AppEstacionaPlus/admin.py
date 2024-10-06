"""from django.contrib import admin
from .models import A_Funcionario, B_Cliente, C_Veiculo, D_EntradaVeiculo, E_SaidaVeiculo

admin.site.register(A_Funcionario)
admin.site.register(B_Cliente)
admin.site.register(C_Veiculo)
admin.site.register(D_EntradaVeiculo)
admin.site.register(E_SaidaVeiculo)

class D_EntradaVeiculoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'funcionario', 'hora_entrada', 'data_entrada')

class E_SaidaVeiculoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'funcionario', 'hora_saida', 'data_saida')"""

from django.contrib import admin
from .models import A_Funcionario, B_Cliente, C_Veiculo, D_EntradaVeiculo, E_SaidaVeiculo

admin.site.register(A_Funcionario)
admin.site.register(B_Cliente)
admin.site.register(C_Veiculo)

class D_EntradaVeiculoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'funcionario', 'hora_entrada', 'data_entrada')

admin.site.register(D_EntradaVeiculo, D_EntradaVeiculoAdmin)


class E_SaidaVeiculoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'funcionario', 'hora_saida', 'data_saida')

admin.site.register(E_SaidaVeiculo, E_SaidaVeiculoAdmin)

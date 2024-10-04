from django.contrib import admin
from .models import A_Funcionario, B_Cliente, C_Veiculo, D_EntradaVeiculo, E_SaidaVeiculo

admin.site.register(A_Funcionario)
admin.site.register(B_Cliente)
admin.site.register(C_Veiculo)
admin.site.register(D_EntradaVeiculo)
admin.site.register(E_SaidaVeiculo)
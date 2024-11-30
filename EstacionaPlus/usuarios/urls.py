from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('EstacionaPlus/', views.EstacionaPlus, name='EstacionaPlus'),
    path('registrar_entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('registrar_saida/', views.registrar_saida, name='registrar_saida'),
    
    
]
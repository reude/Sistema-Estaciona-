from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('EstacionaPlus/', views.EstacionaPlus, name='EstacionaPlus')
    
]
import uuid
import requests
from django.db.models import Sum
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _
import random
from datetime import date, timedelta


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

#Funcionario
class Funcionario(models.Model):
    TURNO = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    ]
    nome = models.CharField(_('Nome'),max_length=100)
    CPF = models.CharField(_('CPF'), max_length=11, unique=True)
    telefone = models.CharField(_('Telefone'), max_length=11, blank=True, null=True)
    email = models.EmailField(_('E-Mail'), blank=True, null=True)
    numero_identificacao = models.AutoField(primary_key=True, unique=True, editable=False)
    turno = models.CharField(_('Turno'),choices=TURNO, max_length=5)
    salario = models.DecimalField(_('Salario'), max_digits=10, decimal_places=2)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    def __str__(self):
        return f'Funcionário(a): {self.nome} - {self.numero_identificacao}'

    class Meta:
        verbose_name = _('Funcionario')
        verbose_name_plural = _('Funcionarios')

# Cliente
class Cliente(models.Model):
    nome = models.CharField(_('Nome'),max_length=100)
    CPF = models.CharField(_('CPF'), max_length=11, unique=True, primary_key=True)
    telefone = models.CharField(_('Telefone'), max_length=11, blank=True, null=True)
    email = models.EmailField(_('E-Mail'), blank=True, null=True)

    def __str__(self):
        return f'Cliente: {self.nome} - CPF: {self.CPF}'
    
    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

# Veículo
class Veiculo(models.Model):
    TIPO_VEICULO = [
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
    ]
    placa = models.CharField(_('Placa'),max_length=7, unique=True, primary_key=True)
    modelo = models.CharField(_('Modelo'),max_length=50)
    cor = models.CharField(_('Cor'),max_length=30)
    tipo = models.CharField(_('Tipo'),choices=TIPO_VEICULO)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)  

    def __str__(self):
        cliente_nome = self.cliente.nome
        return f'Cliente: {cliente_nome} - {self.modelo} ({self.placa})'
    
    class Meta:
        verbose_name = _('Veiculo')
        verbose_name_plural = _('Veiculos')

# EntradaVeículo
class Entrada(models.Model):
    dataHora = models.DateTimeField(_('Data e Hora'), auto_now_add=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('Entrada')
        verbose_name_plural = _('Entradas')


# SaidaVeículo
class Saida(models.Model):
    dataHora = models.DateTimeField(_('Data e Hora'), auto_now_add=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Saida')
        verbose_name_plural = _('Saidas')
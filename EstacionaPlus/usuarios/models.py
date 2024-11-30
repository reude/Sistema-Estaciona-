from django.db import models
from django.contrib.auth.models import User

class VeiculoSet(models.Model):
    TIPO_VEICULO = [
        ('carro', 'Carro'),
        ('moto', 'Moto'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="veiculos")
    modelo = models.CharField(max_length=100)
    tipo_veiculo = models.CharField(max_length=5, choices=TIPO_VEICULO)
    placa = models.CharField(max_length=10)
    publico = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.modelo} - {self.placa}"

class EntradaSet(models.Model):
    veiculo = models.ForeignKey(VeiculoSet, on_delete=models.CASCADE, related_name="entradas")
    data_entrada = models.DateField()
    hora_entrada = models.TimeField()

    def __str__(self):
        return f"{self.veiculo.modelo} - {self.data_entrada} {self.hora_entrada}"

class SaidaSet(models.Model):
    veiculo = models.ForeignKey(VeiculoSet, on_delete=models.CASCADE, related_name="saidas")
    data_saida = models.DateField()
    hora_saida = models.TimeField()

    def __str__(self):
        return f"{self.veiculo.modelo} - {self.data_saida} {self.hora_saida}"

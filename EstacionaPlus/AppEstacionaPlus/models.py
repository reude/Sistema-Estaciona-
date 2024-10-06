from django.db import models
from django.utils import timezone

# Funcionario
class A_Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    numero_identificacao = models.CharField(max_length=10, unique=True)
    turno = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Funcionário: {self.nome} - {self.numero_identificacao}'

    def cadastrar_veiculo(self):
        pass

    def registrar_entrada(self):
        pass

    def registrar_saida(self):
        pass

# Cliente
class B_Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'Cliente: {self.nome} - CPF: {self.cpf}'

    def registrar_cliente(self):
        pass

    def atualizar_dados(self):
        pass

# Veículo
class C_Veiculo(models.Model):
    TIPO_VEICULO = [
        ('carro', 'Carro'),
        ('moto', 'Moto'),
    ]
    placa = models.CharField(max_length=7, unique=True)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=30)
    tipo = models.CharField(choices=TIPO_VEICULO)
    cliente = models.ForeignKey(B_Cliente, on_delete=models.SET_NULL, null=True)  

    def __str__(self):
        cliente_nome = self.cliente.nome if self.cliente else "Sem cliente"
        return f'Cliente: {cliente_nome} - {self.modelo} ({self.placa})'

    def registrar_entrada(self):
        pass

    def registrar_saida(self):
        pass

# EntradaVeículo
class D_EntradaVeiculo(models.Model):
    data_entrada = models.DateField(default=timezone.now) 
    hora_entrada = models.TimeField(default=timezone.now) 
    veiculo = models.ForeignKey(C_Veiculo, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(A_Funcionario, on_delete=models.CASCADE)

    def registrar_entrada(self):
        pass

# SaidaVeículo
class E_SaidaVeiculo(models.Model):
    data_saida = models.DateField(default=timezone.now)  
    hora_saida = models.TimeField(default=timezone.now)  
    veiculo = models.ForeignKey(C_Veiculo, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(A_Funcionario, on_delete=models.CASCADE)

    def registrar_saida(self):
        pass

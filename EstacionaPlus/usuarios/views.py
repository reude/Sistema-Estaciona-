from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from AppEstacionaPlus.models import Veiculo, Entrada, Saida

def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        has_error = False

        # Verificar se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um usuário com esse nome.')
            has_error = True
        
        # Verificar se o e-mail já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Já existe um usuário com esse e-mail.')
            has_error = True

        # Validando se as senhas coincidem
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            has_error = True

        if has_error:
            return render(request, 'cadastro.html', {
                'username': username,
                'email': email,
            })

        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.success(request, 'Cadastro realizado com sucesso!')

        return render(request, 'cadastro.html', {'redirect': True})

    return render(request, 'cadastro.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username') 
        senha = request.POST.get('senha')  

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('EstacionaPlus')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, 'login.html')


def EstacionaPlus(request):
    cliente = request.user
    carros = Veiculo.objects.filter(cliente__email=cliente.email)
    if request.method == "POST":
        # Receber dados do formulário
        veiculo_id = request.POST.get('veiculo')
        data_hora_entrada = request.POST.get('data_entrada')
        data_hora_saida = request.POST.get('data_saida')

        # Validar e salvar a entrada/saída
        try:
            veiculo = Veiculo.objects.get(placa=veiculo_id)
            
            # Registrar entrada ou saída
            if data_hora_entrada:
                Entrada.objects.create(veiculo=veiculo, funcionario=None, dataHora=data_hora_entrada)
                messages.success(request, 'Entrada registrada com sucesso!')
            if data_hora_saida:
                Saida.objects.create(veiculo=veiculo, funcionario=None, dataHora=data_hora_saida)
                messages.success(request, 'Saída registrada com sucesso!')
        except Veiculo.DoesNotExist:
            messages.error(request, 'Veículo não encontrado!')

        return redirect('estaciona_plus')

    return render(request, 'EstacionaPlus.html', {'carros': carros})

            
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import EntradaSet, SaidaSet, VeiculoSet


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        has_error = False

        # Verifica se o nome do usuario ja existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um usuário com esse nome.')
            has_error = True
        
        # Verifica se o e-mail ja existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Já existe um usuário com esse e-mail.')
            has_error = True

        # Verifica se as senhas coincidem
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


@login_required
def EstacionaPlus(request):
    veiculos = VeiculoSet.objects.filter(cliente=request.user)
    entradas = EntradaSet.objects.filter(usuario=request.user)
    saidas = SaidaSet.objects.filter(usuario=request.user)

    context = {
        'veiculos': veiculos,
        'entradas': entradas,
        'saidas': saidas,
    }
    return render(request, 'EstacionaPlus.html', context)

@login_required
def registrar_entrada(request):
    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        data_entrada = request.POST.get('data_entrada')
        hora_entrada = request.POST.get('hora_entrada')

        try:
            veiculo = VeiculoSet.objects.get(id=veiculo_id)
        except VeiculoSet.DoesNotExist:
            return render(request, 'erro.html', {'mensagem': 'Veículo não encontrado!'})

        EntradaSet.objects.create(
            veiculo=veiculo,
            usuario=request.user,
            data_entrada=data_entrada,
            hora_entrada=hora_entrada
        )
        return redirect('EstacionaPlus')

    veiculos = VeiculoSet.objects.filter(publico=True) | VeiculoSet.objects.filter(cliente=request.user)
    return render(request, 'entrada.html', {'veiculos': veiculos})

@login_required
def registrar_saida(request):
    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        data_saida = request.POST.get('data_saida')
        hora_saida = request.POST.get('hora_saida')

        try:
            veiculo = VeiculoSet.objects.get(id=veiculo_id)
        except VeiculoSet.DoesNotExist:
            return render(request, 'erro.html', {'mensagem': 'Veículo não encontrado!'})

        SaidaSet.objects.create(
            veiculo=veiculo,
            usuario=request.user,
            data_saida=data_saida,
            hora_saida=hora_saida
        )
        return redirect('EstacionaPlus')

    veiculos = VeiculoSet.objects.filter(publico=True) | VeiculoSet.objects.filter(cliente=request.user)
    return render(request, 'saida.html', {'veiculos': veiculos})
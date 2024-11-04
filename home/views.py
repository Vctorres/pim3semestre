from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')  # Redireciona para a página inicial após login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

##def login_view(request):
  ##  return render(request, 'login.html')

def sintomas_view(request):
    return render(request, 'sintomas.html')

def atend_view(request):
    return render(request, 'atend.html')

def cadastro_pet_view(request):
    return render(request, 'CadastroPet.html')

def cadastro_funcio_view(request):
    return render(request, 'CadFuncio.html')

def home_view(request):
    return render(request, 'home.html')

def sobrenos_view(request):
    return render(request, 'sobrenos.html')

def comentarios_view(request):
    return render(request, 'comentarios.html')

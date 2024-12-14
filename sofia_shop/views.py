from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, 'about.html')

def account(request):
    return render(request, 'account.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def details(request):
    return render(request, 'details.html')

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def products(request):
    return render(request, 'products.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                message = "Usuario ya existe!"
                return render(request, 'signup.html',{
                    'form': UserCreationForm, 'message': message
                })
            except:
                message = "Usuario ya existe!"
                return render(request, 'signup.html',{
                    'form': UserCreationForm, 'message': message
                })
            
        return HttpResponse('Contraseñas no coinciden!')
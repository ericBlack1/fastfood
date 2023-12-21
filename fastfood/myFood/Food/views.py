from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza, Burger
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    context = {
        'active_link': 'index'
    }
    return render(request, 'food/index.html', context)

def pizza(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas,
        'active_link': 'pizza'
    }
    return render(request, 'food/pizza.html', context)
 
def burger(request):
    burgers = Burger.objects.all()
    context = {
        'burgers': burgers,
        'active_link': 'burger'
    }
    return render(request, 'food/burgers.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@csrf_exempt
def order(request):
    if is_ajax(request):
        note = request.POST.get('note')
        print(note)
    context = {
        'active_link': 'order'
    }
    return render(request, 'food/order.html', context)

def signup(request):
    context = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form'] = form
    else:
        form = NewUserForm()
        context['form'] = form
    return render(request, 'food/signup.html', context)

def logIn(request):
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username and/or password are incorrect')
    context = {
        'active_link': 'login'
    }
    return render(request, 'food/login.html', context)

def logOut(request):
    logout(request)
    return redirect('index')
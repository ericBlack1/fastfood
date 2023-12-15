from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Burger
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

def order(request):
    context = {
        'active_link': 'order'
    }
    return render(request, 'food/order.html', context)
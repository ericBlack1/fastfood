from django.urls import path
from . import views
 
app_name = 'Food'

urlpatterns = [
    path('pizza', views.pizza, name='pizzas'),
    path('burgers', views.burger, name='burgers'),
    path('orders', views.order, name='order'),
]